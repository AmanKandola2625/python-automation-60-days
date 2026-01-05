import requests

from app.config import BASE_URL, TIMEOUT

def fetch_status():
    r = requests.get(BASE_URL, timeout=TIMEOUT)
    r.raise_for_status()
    return r.status_code
