from app.contracts import USER_CONTRACT
from app.validators import validate_contract, validate_status


def test_user_contract(api_client):
    response = api_client.get_user(2)
    validate_status(response, 200)

    body = response.json()
    validate_contract(body, USER_CONTRACT)