from src.personal_account import PersonalAccount
from tests.unit.fixtures import personal_account


class TestPersonalAccountHistory:
    def test_history_transfer(self, personal_account):
        personal_account.balance = 100 
        personal_account.transfer(25, "outgoing")
        personal_account.transfer(35, "outgoing")
        personal_account.transfer(40, "outgoing")
        personal_account.transfer(1, "outgoing")
        personal_account.transfer(5, "incoming")
        assert personal_account.history == [-25, -35, -40, 5]

    def test_history_express_transfer(self, personal_account):
        personal_account.balance = 100 
        personal_account.express_transfer(50)
        personal_account.express_transfer(49)
        assert personal_account.history == [-50, -1, -49, -1]
    
    