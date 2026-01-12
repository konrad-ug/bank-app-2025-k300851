from tests.perf.utils import send_request, send_transfer_request, API_URL


class TestPerformace:
    def test_create_account_100(self):
        for _ in range(100):
            pesel = "87060979383"
            data = {"name": "Jan", "surname": "Kowalski", "pesel": pesel}
            response = send_request(API_URL, "POST", data)
            assert response.status_code == 201
            response = send_request(API_URL + "/" + pesel, "DELETE", {})
            assert response.status_code == 200

    def test_transfer_100(self):
        pesel = "87060979383"
        data = {"name": "Jan", "surname": "Kowalski", "pesel": pesel}
        response = send_request(API_URL, "POST", data)
        assert response.status_code == 201

        for _ in range(100):
            response = send_transfer_request(pesel, 1, "incoming")
            assert response.status_code == 200

        response = send_request(API_URL + "/" + pesel, "GET", {})
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["balance"] == 100

        response = send_request(API_URL + "/" + pesel, "DELETE", {})
        assert response.status_code == 200
