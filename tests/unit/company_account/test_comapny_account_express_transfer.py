from src.comapny_account import ComapnyAccount
from tests.unit.fixtures import company_account
import pytest


class TestCompanyAccountExpressTransfer:
    @pytest.mark.parametrize("balance, amount, balance_after", [
        (100, 95, 0), #valid
        (100, 100, -5), #valid with debt
        (100, -1, 100), #invalid negative amount
        (0, 1, 0) #invalid insufficient balance
    ])
    def test_transfer(self, company_account, balance, amount, balance_after):
        company_account.balance = balance 
        company_account.express_transfer(amount)
        assert company_account.balance == balance_after
