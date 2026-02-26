CREATE_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "job": {"type": "string"},
        "createdAt": {"type": "string"}
    },
    "required": ["id", "name", "job", "createdAt"]
}