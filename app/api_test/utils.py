import json
import requests


def send_request(url: str, type: str, data: dict) -> requests.Response:
        payload = json.dumps(data)
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.request(type, url, headers=headers, data=payload)
        return response
