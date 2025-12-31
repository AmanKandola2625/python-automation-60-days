import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.info("Script started")
logging.warning("This is a warning")
logging.error("This is an error")
logging.info("Script finished")
