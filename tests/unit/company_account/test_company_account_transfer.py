from src.comapny_account import ComapnyAccount


class TestCompanyAccountTransfer:
    def test_transfer_outgoing_valid(self):
        account = ComapnyAccount("Kemar", "587458965")
        account.balance = 100 
        result = account.transfer(100, "outgoing")
        assert account.balance == 0
        assert result == True

    def test_transfer_incoming_valid(self):
        account = ComapnyAccount("Kemar", "587458965")
        account.balance = 100 
        result = account.transfer(5, "incoming")
        assert account.balance == 105
        assert result == True

    def test_transfer_outgoing_negative_amount(self):
        account = ComapnyAccount("Kemar", "587458965")
        account.balance = 100 
        result = account.transfer(-1, "outgoing")
        assert account.balance == 100
        assert result == False

    def test_transfer_incoming_negative_amount(self):
        account = ComapnyAccount("Kemar", "587458965")
        account.balance = 100 
        result = account.transfer(-1, "incoming")
        assert account.balance == 100
        assert result == False

    def test_transfer_outgoing_insufficient_balance(self):
        account = ComapnyAccount("Kemar", "587458965")
        result = account.transfer(1, "outgoing")
        assert account.balance == 0
        assert result == False
    