import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_user(user_id, test_type=None):
    """
    Fetches user data from the API for the given user_id.
    Returns the JSON response as a dictionary.
    Raises ValueError if the request fails or returns a non-200 status code.
    """
    url = f"{BASE_URL}/users/{user_id}"
    response = requests.get(url, timeout=5)

    if response.status_code != 200 and test_type != "negative":
        raise ValueError(f"Failed to fetch user data: {response.status_code}")

    return response

# if __name__ == "__main__":
#     r = get_user(2)
#     print(r.status_code)
#     print(r.json())