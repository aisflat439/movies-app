import json

from django.urls import reverse


def test_suite_works():
    assert "Yee" == "Yee"
    assert "Derp" != "Blah"


def test_ping(client):
    url = reverse("ping")
    response = client.get(url)
    content = json.loads(response.content)
    assert response.status_code == 200
    assert content["ping"] == "pong!"
