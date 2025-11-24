from src.comapny_account import ComapnyAccount
from tests.unit.fixtures import company_account
import pytest


class TestCompanyAccountTransfer:
    @pytest.mark.parametrize("balance, amount, type, balance_after, result", [
        (100, 100, "outgoing", 0, True), #outgoing_valid
        (100, 5, "incoming", 105, True), #incoming_valid
        (100, -1, "outgoing", 100, False), #outgoing_negative_amount
        (100, -1, "incoming", 100, False), #incoming_negative_amount
        (0, 1, "outgoing", 0, False) #outgoing_insufficient_balance
    ])
    def test_transfer(self, company_account, balance, amount, type, balance_after, result):
        company_account.balance = balance 
        result = company_account.transfer(amount, type)
        assert company_account.balance == balance_after
        assert result == result
