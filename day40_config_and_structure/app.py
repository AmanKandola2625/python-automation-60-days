import logging
import requests
from config_reader import load_config

def main():
    config=load_config()

    base_url=config["github"]["base_url"]
    timeout=int(config["github"]["timeout"])
    log_level_str=config["app"].get("log_level","INFO").upper()

    log_level=getattr(logging, log_level_str, logging.INFO)
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    logging.info("Starting Day 40 app")

    r=requests.get(base_url,timeout=timeout)
    r.raise_for_status()

    logging.info("GitHub API reachable")
    logging.info("Finished")

if __name__=="__main__":
    main()

