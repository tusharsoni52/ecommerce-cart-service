from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "UP",
        "service": "cart-service"
    }


def test_add_to_cart():
    response = client.post(
        "/cart",
        json={
            "customer_id": 101,
            "product_id": 1,
            "quantity": 2
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["customer_id"] == 101
    assert data["product_id"] == 1
    assert data["quantity"] == 2
    assert "id" in data


def test_get_cart():
    response = client.get("/cart/101")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    assert data[0]["customer_id"] == 101