from app.api_client import get_user


def test_get_user_success():
    response = get_user(2)

    assert response.status_code == 200

    body = response.json()

    # assert "data" in body
    # assert body["data"]["id"] == 2
    assert body["id"] == 2
    assert "@" in body["email"]

def test_get_user_not_found():
    response = get_user(9999, test_type="negative")

    assert response.status_code == 404

# def test_get_user_not_found():
#     try:
#         get_user(9999)
#     except ValueError as e:
#         assert "Failed to fetch user data" in str(e)
#     else:
#         assert False, "Expected ValueError for non-existent user"