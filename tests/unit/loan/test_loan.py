from src.personal_account import PersonalAccount
from tests.unit.fixtures import personal_account
import pytest


class TestLoan:
    def test_loan_submit_success_last_3_incoming(self, personal_account):
        personal_account.transfer(100, "incoming")
        personal_account.transfer(150, "incoming")
        personal_account.transfer(200, "incoming")
        assert personal_account.submit_for_loan(100) == True
        assert personal_account.balance == 550

    def test_loan_submit_success_sum_5_transactions(self, personal_account):
        personal_account.transfer(200, "incoming")
        personal_account.transfer(50, "outgoing")
        personal_account.transfer(100, "incoming")
        personal_account.transfer(50, "outgoing")
        personal_account.transfer(50, "outgoing")
        assert personal_account.submit_for_loan(100) == True
        assert personal_account.balance == 250

    def test_loan_submit_success_sum_5_transactions_with_express(self, personal_account):
        personal_account.transfer(200, "incoming")
        personal_account.transfer(200, "incoming")
        personal_account.transfer(50, "outgoing")
        personal_account.express_transfer(50)
        assert personal_account.submit_for_loan(100) == True
        assert personal_account.balance == 399

    def test_loan_submit_success_sum_5_transactions_with_2_express(self, personal_account):
        personal_account.transfer(300, "incoming")
        personal_account.express_transfer(50)
        personal_account.express_transfer(50)
        assert personal_account.submit_for_loan(100) == True
        assert personal_account.balance == 298

    @pytest.mark.parametrize("history, amount", [
        ([], 1),
        ([150, 100], 100),
        ([100, 150, -50], 100),
        ([200, -50, 100, -50, -50], 150),
        ([200, -50, 100, -50], 1)
    ])
    def test_loan_submit_fail(self, personal_account, history, amount):
        personal_account = PersonalAccount("John", "Doe", "87060979383")
        personal_account.history = history
        personal_account.balance = sum(history)
        assert personal_account.submit_for_loan(amount) == False
        assert personal_account.balance ==  sum(history)



