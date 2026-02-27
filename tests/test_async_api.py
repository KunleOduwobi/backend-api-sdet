from app.polling import poll_until


def test_get_users_with_delay(api_client):
    def action():
        return api_client.get("/api/users?delay=3")

    def condition(response):
        return response.status_code == 200

    response = poll_until(
        action=action,
        condition=condition,
        timeout=8,
        interval=1
    )

    body = response.json()
    assert "data" in body
    assert len(body["data"]) > 0