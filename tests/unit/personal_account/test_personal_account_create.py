from src.personal_account import PersonalAccount
import pytest


class TestPersonalAccount:
    def test_account_creation(self):
        account = PersonalAccount("John", "Doe", "87060979383")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0
        assert account.national_id == "87060979383"

    @pytest.mark.parametrize("national_id", ["5874589658", "157846987458"])
    def test_account_creation_invalid_national_id(self, national_id):
        account = PersonalAccount("John", "Doe", national_id)
        assert account.national_id == "Invalid"

    def test_account_creation_valid_promo_code(self):
        account = PersonalAccount("John", "Doe", "87060979383", promo_code="PROM_ABC")
        assert account.balance == 50

    @pytest.mark.parametrize("code", [
        "PROMXYZ", "PROM XYZ", "prom_xyz", "", None, "PROM_XYZX", "PPROM_XYZX", "PROM_XY", "PROM_X", "ROM_XYZ"
    ])
    def test_account_creation_invalid_promo_code(self, code): 
        account = PersonalAccount("John", "Doe", "87060979383", promo_code=code)
        assert account.balance == 0, f"Balance should have value 0 with promo code: {code}"

    def test_account_creation_valid_promo_code_year_before_1960(self):
        national_id = "60112574589"
        account = PersonalAccount("John", "Doe", national_id, promo_code="PROM_ABC") 
        assert account.balance == 0
