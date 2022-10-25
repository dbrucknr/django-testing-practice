import json
from django.urls import reverse

def test_account_create(client):
    url = reverse("accounts:create")
    response = client.get(url)
    content = json.loads(response.content)
    assert response.status_code == 200
    assert content["create"] == "created"

def test_account_retrieve(client):
    url = reverse("accounts:retrieve")
    response = client.get(url)
    content = json.loads(response.content)
    assert response.status_code == 200
    assert content["retrieve"] == "retrieved"

def test_account_update(client):
    url = reverse("accounts:update")
    response = client.get(url)
    content = json.loads(response.content)
    assert response.status_code == 200
    assert content["update"] == "updated"

def test_account_delete(client):
    url = reverse("accounts:delete")
    response = client.get(url)
    content = json.loads(response.content)
    assert response.status_code == 200
    assert content["delete"] == "deleted"