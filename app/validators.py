from jsonschema import validate


def validate_status(response, expected_status):
    if response.status_code != expected_status:
        raise AssertionError(
            f"Expected {expected_status}, got {response.status_code}"
        )


def validate_user_schema(body):
    if "data" not in body:
        raise AssertionError("Missing 'data' field")

    required_fields = ["id", "email", "first_name", "last_name"]

    for field in required_fields:
        if field not in body["data"]:
            raise AssertionError(f"Missing field: {field}")
    
    # assert @ in email
    if "@" not in body["data"]["email"]:
        raise AssertionError("Invalid email format")

def validate_schema(body, schema):
    validate(instance=body, schema=schema)

# same as validate_schema but with a custom error message
def validate_contract(response_json, contract):
    validate(instance=response_json, schema=contract)
