from app import create_app


def test_health():
    client = create_app({"TESTING": True}).test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_fees_endpoint():
    client = create_app({"TESTING": True}).test_client()
    response = client.get("/fees?origin=douala&destination=yaounde&weight=8")
    assert response.get_json()["fee"] == 2100
