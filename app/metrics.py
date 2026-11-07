import time

from flask import g, request
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest

REQUESTS = Counter(
    "camtrack_http_requests_total", "Requêtes HTTP", ["method", "endpoint", "status"]
)
LATENCY = Histogram("camtrack_http_request_seconds", "Durée des requêtes", ["endpoint"])


def init_metrics(app):
    @app.before_request
    def start_timer():
        g.start = time.perf_counter()

    @app.after_request
    def record(response):
        endpoint = request.endpoint or "unknown"
        LATENCY.labels(endpoint).observe(time.perf_counter() - g.start)
        REQUESTS.labels(request.method, endpoint, response.status_code).inc()
        return response

    @app.get("/metrics")
    def metrics():
        return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}
