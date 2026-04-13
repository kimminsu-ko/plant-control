from app.server_client import send_event
from app.simulator import make_measurement


def main() -> None:
    event = make_measurement()
    send_event(event)


if __name__ == "__main__":
    main()
