import pytest
from tests.api.account_utils import send_request, API_URL, send_transfer_request


@pytest.fixture
def api_account():
    data = {
            "name": "Jan",
            "surname": "Kowalski",
            "pesel": "87060979383"
    }
    send_request(API_URL, "POST", data)
    return data


@pytest.fixture
def api_account_with_balance():
    data = {
            "name": "Ada",
            "surname": "Nowak",
            "pesel": "66010862393"
    }
    send_request(API_URL , "POST", data)
    send_transfer_request(data["pesel"], 10000, "incoming")
    return data


@pytest.fixture()
def api_clear_registry():
        response = send_request(API_URL, "GET", {})
        accounts = response.json()

        for account in accounts:
            pesel = account["pesel"]
            send_request(f"{API_URL}/{pesel}", "DELETE", {})
