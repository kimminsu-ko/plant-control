import os

import requests


SERVER_URL = os.getenv(
    "SERVER_URL",
    "http://127.0.0.1:5000/api/v1/edge/events",
)


def send_event(event: dict) -> None:
    response = requests.post(SERVER_URL, json=event, timeout=5)
    print(response.status_code, response.text)
