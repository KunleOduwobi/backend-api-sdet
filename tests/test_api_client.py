import pytest

from app.payloads import create_user_payload
from app.validators import validate_status, validate_user_schema, validate_schema
from app.schemas import CREATE_USER_SCHEMA

@pytest.mark.smoke
def test_get_user_success(api_client):
    response = api_client.get_user(2)
    print(f"Response JSON: {response.json()}")  # Debugging statement
    validate_status(response, 200)
    validate_user_schema(response.json())

def test_get_user_not_found(api_client):
    response = api_client.get_user(9999, test_type="negative")
    validate_status(response, 404)

def test_create_user(api_client):
    payload = create_user_payload("Kunle", "QA Engineer")

    response = api_client.post("/api/users", payload)

    validate_status(response, 201)

    body = response.json()
    assert body["name"] == "Kunle"
    assert body["job"] == "QA Engineer"
    assert "id" in body

@pytest.mark.parametrize(
    "name,job",
    [
        ("Alice", "Developer"),
        ("Bob", "Tester"),
        ("Charlie", "Manager"),
    ]
)
def test_create_user_multiple(api_client, name, job):
    payload = create_user_payload(name, job)
    response = api_client.post("/api/users", payload)

    validate_status(response, 201)

    body = response.json()
    assert body["name"] == name
    assert body["job"] == job

def test_create_user_schema(api_client):
    payload = create_user_payload("SchemaUser", "Validator")

    response = api_client.post("/api/users", payload)
    validate_status(response, 201)

    body = response.json()
    validate_schema(body, CREATE_USER_SCHEMA)

@pytest.mark.skip(reason="Skipping invalid payload test")
def test_create_user_invalid_payload(api_client):
    payload = {"name": "InvalidUser"}  # Missing 'job' field

    response = api_client.post("/api/users", payload)
    validate_status(response, 400)

def test_print_total_users(api_client):
    response = api_client.get("/api/users")
    validate_status(response, 200)

    body = response.json()
    total_users = body.get("total", 0)
    print(f"Total users: {total_users}")

def test_print_last_user_id_and_name(api_client):
    response = api_client.get("/api/users")
    validate_status(response, 200)

    body = response.json()
    users = body.get("data", [])
    if users:
        last_user = users[-1]
        print(f"Last user ID: {last_user['id']}, Name: {last_user['first_name']} {last_user['last_name']}")
    else:
        print("No users found")

# def test_get_user_not_found():
#     try:
#         get_user(9999)
#     except ValueError as e:
#         assert "Failed to fetch user data" in str(e)
#     else:
#         assert False, "Expected ValueError for non-existent user"