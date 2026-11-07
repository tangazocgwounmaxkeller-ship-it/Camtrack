import os

from flask import Flask, jsonify, request

from .fees import delivery_fee
from .metrics import init_metrics


def create_app(config: dict | None = None) -> Flask:
    app = Flask(__name__)
    app.config["DATABASE_URL"] = os.environ.get("DATABASE_URL", "sqlite:///camtrack.db")
    if config:
        app.config.update(config)
    init_metrics(app)

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/fees")
    def fees():
        try:
            origin = request.args["origin"].lower()
            destination = request.args["destination"].lower()
            weight = float(request.args["weight"])
        except (KeyError, ValueError):
            return jsonify(error="paramètres invalides"), 400
        return jsonify(fee=delivery_fee(origin, destination, weight), currency="XAF")

    return app
