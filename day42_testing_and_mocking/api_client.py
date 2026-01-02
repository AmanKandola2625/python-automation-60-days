import requests

def fetch_status(url: str) -> int:
    r = requests.get(url, timeout=5)
    r.raise_for_status()
    return r.status_code
