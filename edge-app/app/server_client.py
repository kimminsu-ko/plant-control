import requests


SERVER_URL = "http://server-app:5000/api/v1/edge/events"


def send_event(event: dict) -> None:
    response = requests.post(SERVER_URL, json=event, timeout=5)
    print(response.status_code, response.text)
