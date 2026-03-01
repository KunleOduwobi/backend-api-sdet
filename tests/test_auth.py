

import pytest

from app.validators import validate_status


@pytest.mark.smoke
def test_login_success(api_client):
    login_response = api_client.login(
        email="eve.holt@reqres.in",
        password="cityslicka"
    )
    validate_status(login_response, 200)
    body = login_response.json()
    assert "token" in body

    user_response = api_client.get_user(2)
    validate_status(user_response, 200)

    
