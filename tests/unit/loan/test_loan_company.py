from tests.unit.fixtures import company_account
import pytest


class TestLoanCompany:
    @pytest.mark.parametrize("history, amount, result, balance_after", [
        ([1777, -1775], 1, True, 3), #valid amount and ZUS
        ([1776, -1775], 1, False, 1), #invalid amount valid ZUS
        ([2], 1, False, 2), #valid amount invalid ZUS
        ([2, 1775], 1, False, 1777), #1775 not negative (invalid zus)
        ([1777, -1775], -1, False, 2) #negative amount
    ])
    def test_loan(self, company_account, history, amount, result, balance_after):
        company_account.history = history
        company_account.balance = sum(history)
        assert company_account.take_loan(amount) == result
        assert company_account.balance == balance_after
