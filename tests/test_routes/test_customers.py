import json


def test_create_customer(client):
    data = {"username":"testuser", "email":"testemail@gmail.com", "password":"testing"}
    response = client.post("/customers/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "testemail@gmail.com"