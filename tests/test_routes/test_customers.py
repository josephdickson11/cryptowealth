import json


def test_create_customer(client):
    data = {"username":"testuser", "email":"tesdail@gmail.com", "password":"testing"}
    response = client.post("/customers", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "testemail@gmail.com"
    assert response.json()["is_KYC"] == False