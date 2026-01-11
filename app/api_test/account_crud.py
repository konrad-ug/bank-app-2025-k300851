import pytest
from app.api_test.utils import send_request
from app.api_test.fixtures import API_URL, api_account



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
    