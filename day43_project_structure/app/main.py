import logging

from app.client import fetch_status

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    status = fetch_status()
    logging.info(f"Fetched status code: {status}")

if __name__ == "__main__":
    main()
