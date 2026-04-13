from datetime import datetime, timezone


def make_measurement() -> dict:
    return {
        "event_type": "measurement",
        "resource_type": "solar",
        "equipment_id": "solar-01",
        "occurred_at": datetime.now(timezone.utc).isoformat(),
        "payload": {
            "P": 120.5,
            "Q": 15.2,
            "V": 380.0,
            "I": 182.0,
            "f": 60.0,
            "PF": 0.99,
        },
    }
