

from src.personal_account import PersonalAccount


class TestCompanyAccountExpressTransfer:
    def test_transfer_valid(self):
        account = PersonalAccount("John", "Doe", "87060979383")
        account.balance = 100 
        account.express_transfer(99)
        assert account.balance == 0

    def test_transfer_valid_with_debt(self):
        account = PersonalAccount("John", "Doe", "87060979383")
        account.balance = 100 
        account.express_transfer(100)
        assert account.balance == -1

    def test_transfer_negative_amount(self):
        account = PersonalAccount("John", "Doe", "87060979383")
        account.balance = 100 
        account.express_transfer(-1)
        assert account.balance == 100

    def test_transfer_insufficient_balance(self):
        account = PersonalAccount("John", "Doe", "87060979383")
        account.express_transfer(1)
        assert account.balance == 0
