import pytest
from tests.api.account_utils import send_request, send_transfer_request
from tests.api.fixtures import API_URL, api_account, api_account_with_balance, api_clear_registry



class TestAccountDatabase:
    def test_save_and_load(self, api_clear_registry, api_account_with_balance):
        send_request(API_URL + "/save", "POST", {})
        send_request(API_URL + "/load", "POST", {})
        response = send_request(API_URL, "GET", {})
        assert response.status_code == 200
        accounts = response.json()
        assert len(accounts) == 1
        assert api_account_with_balance["name"] == accounts[0]["name"]
        assert api_account_with_balance["surname"] == accounts[0]["surname"]
        assert api_account_with_balance["pesel"] == accounts[0]["pesel"]
        assert accounts[0]["balance"] == 10000
