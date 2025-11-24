import re
from src.national_id_utils import get_year_from_national_id
from src.account import Account


class PersonalAccount(Account):
    def __init__(self, first_name, last_name, national_id, promo_code=None):
        super().__init__(trasnfer_fee=-1)
        self.first_name = first_name
        self.last_name = last_name

        national_id_year = get_year_from_national_id(national_id)
        if national_id_year is None:
            national_id = "Invalid"
        self.national_id = national_id

        if promo_code is not None and re.match(r"^PROM_...$", promo_code) and national_id_year and national_id_year > 1960:
            self.balance += 50

    def submit_for_loan(self, amount):
        #Ostatnie trzy zaksięgowane transakcje powinny być transakcjami wpłaty
        if len(self.history) >= 3:
            last_3 = self.history[-3:]
            if all(x > 0 for x in last_3):
                self.balance += amount
                return True
        #Suma ostatnich pięciu transakcji (konto musi mieć co najmniej pięć transakcji) powinna być większa niż kwota wnioskowanego kredytu. 
        if len(self.history) >= 5:
            last_5 = self.history[-5:]
            if sum(last_5) > amount:
                self.balance += amount
                return True
            
        return False
