import pytest
import responses
from app.api_client import APIClient

@pytest.mark.mocked
@responses.activate
def test_get_user_mocked():
    client = APIClient("https://reqres.in", api_key="dummy")

    responses.add(
        method=responses.GET,
        url="https://reqres.in/api/users/2",
        json={"data": {"id": 2, "email": "x@y.com", "first_name": "A", "last_name": "B"}},
        status=200
    )

    r = client.get_user(2)
    assert r.status_code == 200
    assert r.json()["data"]["id"] == 2