from datetime import date
import json

from starlette.responses import Response


def test_create_accounts(client):
    data = {"wallet_address": "ldhglhgirgkoslkdg"
    }

    response = client.post("/normal_accounts/create-account/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["wallet_address"] == "ldhglhgirgkoslkdg"