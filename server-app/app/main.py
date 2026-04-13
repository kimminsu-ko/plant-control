from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.post("/api/v1/edge/events")
def ingest_edge_event():
    payload = request.get_json(silent=True) or {}
    print("received event:", payload)
    return jsonify({"accepted": True}), 202


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
