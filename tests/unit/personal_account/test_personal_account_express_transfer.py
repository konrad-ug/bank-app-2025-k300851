from src.personal_account import PersonalAccount
from tests.unit.fixtures import personal_account
import pytest


class TestPersonalAccountExpressTransfer:
    @pytest.mark.parametrize("balance, amount, balance_after", [
        (100, 99, 0), #valid
        (100, 100, -1), #valid with debt
        (100, -1, 100), #invalid negative amount
        (0, 1, 0) #invalid insufficient balance
    ])
    def test_transfer(self, personal_account, balance, amount, balance_after):
        personal_account.balance = balance 
        personal_account.express_transfer(amount)
        assert personal_account.balance == balance_after
