from src.comapny_account import ComapnyAccount


class TestComapnyAccount:
    def test_account_create(self):
        account = ComapnyAccount("Kemar", "5874589874")
        assert account.name == "Kemar"
        assert account.nip == "5874589874"

    def test_account_create_invalid_nip(self):
        account = ComapnyAccount("Kemar", "587458987")
        assert account.nip == "Invalid"
    
        account = ComapnyAccount("Kemar", "58745898748")
        assert account.nip == "Invalid"

    