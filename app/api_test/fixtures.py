import pytest
from app.api_test.utils import send_request

API_URL = "http://127.0.0.1:5000/api/accounts"

@pytest.fixture
def api_account():
    data = {
            "name": "Jan",
            "surname": "Kowalski",
            "pesel": "87060979383"
    }
    send_request(API_URL, "POST", data)
    return data
