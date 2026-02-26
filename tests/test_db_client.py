from app.db_client import DBClient


def test_user_api_matches_db(api_client):
    response = api_client.get_user(2)
    assert response.status_code == 200

    api_email = response.json()["data"]["email"]

    db = DBClient("sqlite:///data/test.db")
    row = db.fetch_one(
        "SELECT email FROM users WHERE id = :id",
        {"id": 2}
    )

    assert row is not None
    assert api_email == row[0]