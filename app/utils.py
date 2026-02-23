def is_user_active(response):
    """
    Returns True if:
    - status is 200
    - data exists
    - active field is True
    Otherwise, raises ValueError
    """
    if response.get("status") != 200:
        raise ValueError(f"Expected status 200 but got {response.get('status')}")
    
    data = response.get("data")
    if data is None:
        raise ValueError("Missing 'data' field")
    
    if "active" not in data:
        raise ValueError("Missing 'active' field")

    
    return data["active"]

def get_admin_ids(response):
    """
    Returns a list of admin IDs from the response.
    The response is expected to have the following structure:
    {
        "status": 200,
        "data": {
            "admins": [
                {"id": 1, "name": "Admin1"},
                {"id": 2, "name": "Admin2"}
            ]
        }
    }
    If the structure is invalid, raises ValueError.
    """
    if response.get("status") != 200:
        raise ValueError("Invalid status code")

    data = response.get("data")
    if data is None:
        raise ValueError("Missing 'data' field")

    admins = data.get("admins")
    if not isinstance(admins, list):
        raise ValueError("'admins' must be a list")

    ids = []

    for admin in admins:
        if "id" not in admin:
            raise ValueError("Admin missing 'id' field")
        ids.append(admin["id"])

    return ids
    

def safe_divide(a, b):
    """
    Safely divides a by b, raise ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b