from app.validators import validate_status, validate_user_schema

def test_get_user_success(api_client):
    response = api_client.get_user(2)

    validate_status(response, 200)
    validate_user_schema(response.json())

def test_get_user_not_found(api_client):
    response = api_client.get_user(9999, test_type="negative")
    validate_status(response, 404)

# def test_get_user_not_found():
#     try:
#         get_user(9999)
#     except ValueError as e:
#         assert "Failed to fetch user data" in str(e)
#     else:
#         assert False, "Expected ValueError for non-existent user"