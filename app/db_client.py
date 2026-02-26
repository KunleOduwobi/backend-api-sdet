from sqlalchemy import create_engine, text


class DBClient:

    def __init__(self, db_url):
        self.engine = create_engine(db_url)

    def fetch_one(self, query, params=None):
        with self.engine.connect() as conn:
            result = conn.execute(text(query), params or {})
            return result.fetchone()