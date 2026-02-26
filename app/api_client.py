from urllib import response

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


class APIClient:

    def __init__(self, base_url, api_key):
        self.base_url = base_url
        # print the initialized base URL for debugging
        print(f"APIClient initialized with base URL: {self.base_url}")
        self.headers = {"x-api-key": api_key}

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return requests.get(url, headers=self.headers, timeout=5)

    def post(self, endpoint, payload):
        url = f"{self.base_url}{endpoint}"
        print(f"POST {url}")
        response = requests.post(
            url,
            json=payload,
            headers=self.headers,
            timeout=5
        )
        print(f"Status: {response.status_code}")
        return response

    def get_user(self, user_id, test_type=None):
        response = self.get(f"/api/users/{user_id}")
        print(
            f"GET /api/users/{user_id} - Status Code: {response.status_code}"
        )  # Debugging statement
        if response.status_code != 200 and test_type != "negative":
            raise ValueError(f"Failed to fetch user data: {response.status_code}")
        return response
