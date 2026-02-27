USER_CONTRACT = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "number"},
                "email": {"type": "string"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"}
            },
            "required": ["id", "email", "first_name", "last_name"]
        }
    },
    "required": ["data"]
}