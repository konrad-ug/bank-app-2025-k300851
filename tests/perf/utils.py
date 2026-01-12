import json
import requests

API_URL = "http://127.0.0.1:5000/api/accounts"

def send_request(url: str, type: str, data: dict) -> requests.Response:
        payload = json.dumps(data)
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.request(type, url, headers=headers, data=payload)
        return response


def send_transfer_request(national_id: str, amount: int, type: str):
        data = {
                "amount": amount,
                "type": type
        }
        return send_request(f"{API_URL}/{national_id}/transfer", "POST", data)
