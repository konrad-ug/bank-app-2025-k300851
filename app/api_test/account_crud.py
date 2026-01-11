import pytest
from app.api_test.account_utils import send_request, send_transfer_request
from app.api_test.fixtures import API_URL, api_account, api_account_with_balance



class TestAccountCrud:
    def test_create_account(self):
        data = {
            "name": "Jan",
            "surname": "Kowalski",
            "pesel": "87060979383"
        }
        response = send_request(API_URL, "POST", data)
        assert response.status_code == 201
        response_data = response.json()
        assert response_data["message"] == "Account created"

    def test_create_account_with_the_same_national_id(self, api_account):
        response = send_request(API_URL, "POST", api_account)
        assert response.status_code == 409
        response_data = response.json()
        assert response_data["message"] == "Account with pesel 87060979383 is already exist"

    def test_get_account(self, api_account):
        response = send_request(API_URL + "/" + api_account["pesel"], "GET", {})
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["pesel"] == api_account["pesel"]
        assert response_data["name"] == api_account["name"]
        assert response_data["surname"] == api_account["surname"]
        assert response_data["balance"] == 0

    def test_get_account_not_found(self):
        response = send_request(API_URL + "/08220638782", "GET", {})
        assert response.status_code == 404
    
    def test_update_account(self, api_account):
        data = {
            "pesel": "53072356799",
            "name": "Tomasz",
            "surname": "Nowak"
        }
        response = send_request(API_URL + "/" + api_account["pesel"], "PATCH", data)
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["message"] == "Account updated"

    def test_delete_account(self, api_account):
        response = send_request(API_URL + "/" + api_account["pesel"], "DELETE", {})
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["message"] == "Account deleted"


    @pytest.mark.parametrize("type", ["express", "incoming", "outgoing"])
    def test_account_transfer(self, api_account_with_balance, type):
        response = send_transfer_request(api_account_with_balance["pesel"], 1, type)
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["message"] == "Zlecenie przyjęto do realizacji"

    def test_account_transfer_invalid_account(self):
        response = send_transfer_request("63052847478", 1, "incoming")
        assert response.status_code == 404
        response_data = response.json()
        assert response_data["message"] == "Account not exists"

    def test_account_transfer_invalid_type(self, api_account_with_balance):
        response = send_transfer_request(api_account_with_balance["pesel"], 1, "expres")
        assert response.status_code == 422
        response_data = response.json()
        assert response_data["message"] == "Type is invalid"

    @pytest.mark.parametrize("type", ["express", "outgoing"])
    def test_account_transfer_insufficient_balance(self, api_account, type):
        response = send_transfer_request(api_account["pesel"], 1, type)
        assert response.status_code == 422
        response_data = response.json()
        assert response_data["message"] == "Transaction error"

    @pytest.mark.parametrize("type", ["express", "outgoing", "incoming"])
    def test_account_transfer_negative_amount(self, api_account_with_balance, type):
        response = send_transfer_request(api_account_with_balance["pesel"], -1, type)
        assert response.status_code == 422
        response_data = response.json()
        assert response_data["message"] == "Transaction error"
