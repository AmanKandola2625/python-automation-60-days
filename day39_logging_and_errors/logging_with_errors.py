import logging
import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def fetch_url(url: str):
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        logging.info("Fetched data successfully")
    except requests.exceptions.Timeout:
        logging.error("Request timed out")
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    fetch_url("https://api.github.com/invalid-endpoint")
