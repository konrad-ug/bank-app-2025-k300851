from src.account import Account
import requests
from datetime import datetime
import os

VAT_API_URL = os.getenv("BANK_APP_MF_URL", "https://wl-test.mf.gov.pl/api/search/nip").strip()

class CompanyAccount(Account): # pragma: no cover
    def __init__(self, name, nip):
        super().__init__(trasnfer_fee=-5)
        self.name = name
        if len(nip) != 10:
            nip = "Invalid"
        elif not self.check_nip(nip):
            raise ValueError("Company not registered!!")
        self.nip = nip
 
    def take_loan(self, amount):
        if amount <= 0 or -1775 not in self.history or 2 * amount > self.balance:
            return False
        self.balance += amount
        return True
    
    def check_nip(self, nip):
        response = requests.get(f"{VAT_API_URL}/{nip}", params={"date": datetime.now().strftime("%Y-%m-%d") })
        if response.status_code == 200:
            data = response.json()
            if data["result"] is None or data["result"]["subject"] is None:
                return False
            status_vat = data["result"]["subject"]["statusVat"]
            print(nip, "status vat:", status_vat)
            return status_vat == "Czynny"
        return False
        