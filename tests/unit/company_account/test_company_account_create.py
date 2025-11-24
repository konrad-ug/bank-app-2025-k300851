from src.comapny_account import ComapnyAccount
import pytest


class TestComapnyAccount:
    def test_account_create(self):
        account = ComapnyAccount("Kemar", "5874589874")
        assert account.name == "Kemar"
        assert account.nip == "5874589874"

    @pytest.mark.parametrize("nip", ["587458987", "58745898748"])
    def test_account_create_invalid_nip(self, nip):
        account = ComapnyAccount("Kemar", nip)
        assert account.nip == "Invalid"
    
