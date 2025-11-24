from src.comapny_account import ComapnyAccount
from tests.unit.fixtures import company_account


class TestComapnyAccountHistory:
    def test_history_transfer(self, company_account):
        company_account.balance = 100 
        company_account.transfer(25, "outgoing")
        company_account.transfer(35, "outgoing")
        company_account.transfer(40, "outgoing")
        company_account.transfer(1, "outgoing")
        company_account.transfer(5, "incoming")
        assert company_account.history == [-25, -35, -40, 5]

    def test_history_express_transfer(self, company_account):
        company_account = ComapnyAccount("Kemar", "587458965")
        company_account.balance = 100 
        company_account.express_transfer(50)
        company_account.express_transfer(45)
        assert company_account.history == [-50, -5, -45, -5]
    