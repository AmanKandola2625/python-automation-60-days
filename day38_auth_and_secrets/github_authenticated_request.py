import os
import requests
import sys

def headers():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("ERROR: GITHUB_TOKEN not set")
        sys.exit(1)

    return {
        "Accept": "application/vnd.github+json",
        "User-Agent": "python-automation-day38",
        "Authorization": f"Bearer {token}",
    }

def main():
    url = "https://api.github.com/user"
    r = requests.get(url, headers=headers(), timeout=30)
    r.raise_for_status()

    data = r.json()
    print("Authenticated as:", data["login"])

if __name__ == "__main__":
    main()
