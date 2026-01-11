from tests.unit.fixtures import personal_account, company_account, accounts_registry_empty, accounts_registry_filled
import pytest


class TestAccountsRegistry:
    def test_add_account_valid(self, accounts_registry_empty, personal_account):
        accounts_registry_empty.add_account(personal_account)
        assert len(accounts_registry_empty.accounts) == 1
        assert accounts_registry_empty.accounts[0].national_id == personal_account.national_id

    def test_add_accounts_with_the_same_national_id(self, accounts_registry_empty, personal_account):
        accounts_registry_empty.add_account(personal_account)
        accounts_registry_empty.add_account(personal_account)
        assert len(accounts_registry_empty.accounts) == 1
        assert accounts_registry_empty.accounts[0].national_id == personal_account.national_id

    def test_add_account_company(self, accounts_registry_empty, company_account):
        accounts_registry_empty.add_account(company_account)
        assert len(accounts_registry_empty.accounts) == 0

    def test_add_account_none(self, accounts_registry_empty):
        accounts_registry_empty.add_account(None)
        assert len(accounts_registry_empty.accounts) == 0

    @pytest.mark.parametrize("national_id, result", [
        ("88102073355", True), #valid id
        ("88102073350", False), #invalid id
        (None, False)
    ])
    def test_get_account_not_exists(self, accounts_registry_filled, national_id, result):
        account = accounts_registry_filled.get_by_national_id(national_id)
        if result:
            assert account is not None
            assert account.national_id == national_id
        else:
            assert account is None

    def test_get_all_accounts(self, accounts_registry_filled):
        accounts = accounts_registry_filled.get_all()
        assert len(accounts) == 3

    def test_get_all_account_empty_registry(self, accounts_registry_empty):
        accounts = accounts_registry_empty.get_all()
        assert len(accounts) == 0

    def test_count_account(self, accounts_registry_filled):
        assert accounts_registry_filled.count() == 3

    def test_count_account_empty_registry(self, accounts_registry_empty):
        assert accounts_registry_empty.count() == 0

    def test_update_account(self, accounts_registry_filled):
        data = {
            "name": "Jan",
            "surname": "Kowalski",
            "pesel": "03222467185"
        }
        assert accounts_registry_filled.update("88102073355", data) == True

    def test_update_account_not_exists(self, accounts_registry_filled):
        data = {
            "name": "Jan",
            "surname": "Kowalski",
            "pesel": "03222467185"
        }
        assert accounts_registry_filled.update("62031557434", data) == False

    def test_delete_account(self, accounts_registry_filled):
        accounts_len = len(accounts_registry_filled.accounts)
        assert accounts_registry_filled.delete("88102073355") == True
        assert len(accounts_registry_filled.accounts) == accounts_len - 1

    def test_delete_account_not_exists(self, accounts_registry_filled):
        accounts_len = len(accounts_registry_filled.accounts)
        assert accounts_registry_filled.delete("75062655448") == False
        assert len(accounts_registry_filled.accounts) == accounts_len
