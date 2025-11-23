from src.personal_account import PersonalAccount


class TestPersonalAccountTransfer:
    def test_transfer_outgoing_valid(self):
        account = PersonalAccount("John", "Doe", "87060979383")
        account.balance = 100 
        result = account.transfer(100, "outgoing")
        assert account.balance == 0
        assert result == True

    def test_transfer_incoming_valid(self):
        account = PersonalAccount("John", "Doe", "87060979383")
        account.balance = 100 
        result = account.transfer(5, "incoming")
        assert account.balance == 105
        assert result == True

    def test_transfer_outgoing_negative_amount(self):
        account = PersonalAccount("John", "Doe", "87060979383")
        account.balance = 100 
        result = account.transfer(-1, "outgoing")
        assert account.balance == 100
        assert result == False

    def test_transfer_incoming_negative_amount(self):
        account = PersonalAccount("John", "Doe", "87060979383")
        account.balance = 100 
        result = account.transfer(-1, "incoming")
        assert account.balance == 100
        assert result == False

    def test_transfer_outgoing_insufficient_balance(self):
        account = PersonalAccount("John", "Doe", "87060979383")
        result = account.transfer(1, "outgoing")
        assert account.balance == 0
        assert result == False
    