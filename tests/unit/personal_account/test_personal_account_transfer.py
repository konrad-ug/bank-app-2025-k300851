from src.personal_account import PersonalAccount
from tests.unit.fixtures import personal_account
import pytest


class TestPersonalAccountTransfer:
    @pytest.mark.parametrize("balance, amount, type, balance_after, result", [
        (100, 100, "outgoing", 0, True), #outgoing_valid
        (100, 5, "incoming", 105, True), #incoming_valid
        (100, -1, "outgoing", 100, False), #outgoing_negative_amount
        (100, -1, "incoming", 100, False), #incoming_negative_amount
        (0, 1, "outgoing", 0, False) #outgoing_insufficient_balance
    ])
    def test_transfer(self, personal_account, balance, amount, type, balance_after, result):
        personal_account.balance = balance 
        result = personal_account.transfer(amount, type)
        assert personal_account.balance == balance_after
        assert result == result
