import os

from sqlalchemy import create_engine, text


class DBClient:

    def __init__(self, db_url=None):
        self.db_url = db_url or self._build_db_url()
        self.engine = create_engine(self.db_url)

    def _build_db_url(self):
        db_type = os.getenv("DB_TYPE", "sqlite")

        if db_type == "sqlite":
            return "sqlite:///data/test.db"

        if db_type == "postgres":
            user = os.getenv("DB_USER")
            password = os.getenv("DB_PASSWORD")
            host = os.getenv("DB_HOST")
            port = os.getenv("DB_PORT")
            name = os.getenv("DB_NAME")

            if not all([user, password, host, port, name]):
                raise ValueError("Missing DB environment variables")

            return f"postgresql://{user}:{password}@{host}:{port}/{name}"

        raise ValueError(f"Unsupported DB type: {db_type}")


    def fetch_one(self, query, params=None):
        with self.engine.connect() as conn:
            result = conn.execute(text(query), params or {})
            return result.fetchone()