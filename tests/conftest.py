import pytest
from app.api_client import APIClient
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
import os



@pytest.fixture(scope="session")
def api_client():
    api_key = os.getenv("REQRES_API_KEY")
    if not api_key:
        raise ValueError("API key not found in environment variables")
    return APIClient("https://reqres.in", api_key)