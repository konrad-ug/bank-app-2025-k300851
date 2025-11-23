from src.comapny_account import ComapnyAccount


class TestCompanyAccountExpressTransfer:
    def test_transfer_valid(self):
        account = ComapnyAccount("Kemar", "587458965")
        account.balance = 100 
        account.express_transfer(95)
        assert account.balance == 0

    def test_transfer_valid_with_debt(self):
        account = ComapnyAccount("Kemar", "587458965")
        account.balance = 100 
        account.express_transfer(100)
        assert account.balance == -5

    def test_transfer_negative_amount(self):
        account = ComapnyAccount("Kemar", "587458965")
        account.balance = 100 
        account.express_transfer(-1)
        assert account.balance == 100

    def test_transfer_insufficient_balance(self):
        account = ComapnyAccount("Kemar", "587458965")
        account.express_transfer(1)
        assert account.balance == 0
