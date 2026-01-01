import argparse
import logging
import requests

from configparser import ConfigParser

def load_config(path="config.ini"):
    cfg = ConfigParser()
    cfg.read(path)
    return cfg

def main():
    parser = argparse.ArgumentParser(description="CLI overrides config values")
    parser.add_argument("--timeout", type=int, help="Override timeout")
    args = parser.parse_args()

    config = load_config("../day40_config_and_structure/config.ini")
    timeout = args.timeout if args.timeout is not None else int(config["github"]["timeout"])

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    logging.info(f"Using timeout = {timeout}")
    r = requests.get("https://api.github.com", timeout=timeout)
    r.raise_for_status()
    logging.info("Request succeeded")

if __name__ == "__main__":
    main()
