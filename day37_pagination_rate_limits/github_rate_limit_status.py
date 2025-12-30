import os
import time
from datetime import datetime, timezone

import requests


def headers():
    h = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "python-automation-60-days-day37",
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def fmt_reset(epoch_seconds: int) -> str:
    dt = datetime.fromtimestamp(epoch_seconds, tz=timezone.utc).astimezone()
    return dt.strftime("%Y-%m-%d %H:%M:%S %Z")


def main():
    url = "https://api.github.com/rate_limit"
    r = requests.get(url, headers=headers(), timeout=30)
    r.raise_for_status()
    data = r.json()

    core = data["resources"]["core"]
    print("GitHub Rate Limit (core)")
    print(f"  Limit     : {core['limit']}")
    print(f"  Remaining : {core['remaining']}")
    print(f"  Used      : {core['used']}")
    print(f"  Resets at : {fmt_reset(core['reset'])}")

    # Also show your last response headers if you want:
    # print("X-RateLimit-Remaining:", r.headers.get("X-RateLimit-Remaining"))


if __name__ == "__main__":
    main()
