from app.utils import is_user_active, get_admin_ids, safe_divide


def test_is_user_active():
    response = {
        "status": 200,
        "data": {
            "active": True
        }
    }

    assert is_user_active(response) is True

def test_get_admin_ids():
    response = {
        "status": 200,
        "data": {
            "admins": [
                {"id": 1, "name": "Admin1"},
                {"id": 2, "name": "Admin2"}
            ]
        }
    }
    assert get_admin_ids(response) == [1, 2]

def test_safe_divide():
    assert safe_divide(10, 2) == 5