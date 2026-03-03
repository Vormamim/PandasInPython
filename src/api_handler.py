"""
API Handler Module
Provides tiny helpers to demonstrate fetching and inspecting web APIs.
This version uses a public sample API (JSONPlaceholder) and keeps logic
simple so beginners can follow every step.
"""

import requests
import urllib3

# allow insecure SSL for environments with self-signed certs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_api(url: str) -> bool:
    """Perform a GET request to *url* and return True if the API responds.

    Prints the status code so learners can verify connectivity.
    """
    try:
        resp = requests.get(url, verify=False)
        print(f"API status code: {resp.status_code}")
        return resp.status_code == 200
    except Exception as exc:
        print(f"API check failed: {exc}")
        return False


def fetch_posts() -> list[dict]:
    """Fetch a list of posts from a public test API.

    Uses https://jsonplaceholder.typicode.com/posts which requires no
    authentication and returns JSON suitable for a pandas DataFrame.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    resp = requests.get(url, verify=False)
    resp.raise_for_status()
    return resp.json()
    
def display_raw_data(data, max_items=5) -> None:
    """Display raw API response in formatted way."""
    if not data:
        print("No data to display")
        return
    
    if isinstance(data, list):
        print(f"\n[List with {len(data)} items]")
        print("First few items:")
        for i, item in enumerate(data[:max_items]):
            print(f"\n--- Item {i+1} ---")
            if isinstance(item, dict):
                for key, value in item.items():
                    print(f"  {key}: {value}")
            else:
                print(f"  {item}")
        if len(data) > max_items:
            print(f"\n... and {len(data) - max_items} more items")
            
    elif isinstance(data, dict):
        print("\n[Dictionary]")
        for key, value in data.items():
            if isinstance(value, (list, dict)):
                print(f"  {key}: <{type(value).__name__} with {len(value)} items>")
            else:
                print(f"  {key}: {value}")
    
def list_available_apis() -> None:
    """List the sample JSONPlaceholder API used in the tutorial."""
    print("\n[INFO] Available API: JSONPlaceholder posts")
    print("-" * 60)
    print("  https://jsonplaceholder.typicode.com/posts")



# Quick exercise when running this module directly
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    print("Checking sample API...")
    ok = check_api(url)
    print("API reachable?", ok)

    print("Fetching posts...")
    posts = fetch_posts()
    display_raw_data(posts, max_items=2)
