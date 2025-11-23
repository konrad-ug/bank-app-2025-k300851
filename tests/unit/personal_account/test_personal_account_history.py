from src.personal_account import PersonalAccount


class TestPersonalAccountHistory:
    def test_history_transfer(self):
        account = PersonalAccount("John", "Doe", "87060979383")
        account.balance = 100 
        account.transfer(25, "outgoing")
        account.transfer(35, "outgoing")
        account.transfer(40, "outgoing")
        account.transfer(1, "outgoing")
        account.transfer(5, "incoming")
        assert account.history == [-25, -35, -40, 5]

    def test_history_express_transfer(self):
        account = PersonalAccount("John", "Doe", "87060979383")
        account.balance = 100 
        account.express_transfer(50)
        account.express_transfer(49)
        assert account.history == [-50, -1, -49, -1]
    
    