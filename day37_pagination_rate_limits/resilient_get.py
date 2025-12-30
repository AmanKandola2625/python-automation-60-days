import argparse
import os
import random
import time
from typing import Dict, Optional

import requests


def build_headers() -> Dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "python-automation-60-days-day37",
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def resilient_get(
    session: requests.Session,
    url: str,
    params: Optional[dict] = None,
    max_retries: int = 6,
    timeout: int = 30,
) -> requests.Response:
    """
    Retries on:
      - 429 Too Many Requests
      - 403 (common for secondary rate limit / abuse detection)
      - 5xx transient errors
    Uses:
      - Retry-After header when present
      - Exponential backoff + jitter otherwise
    """
    headers = build_headers()

    for attempt in range(max_retries + 1):
        resp = session.get(url, headers=headers, params=params, timeout=timeout)

        if resp.status_code < 400:
            return resp

        retry_after = resp.headers.get("Retry-After")
        remaining = resp.headers.get("X-RateLimit-Remaining")
        reset = resp.headers.get("X-RateLimit-Reset")

        should_retry = resp.status_code in (429, 403) or 500 <= resp.status_code <= 599
        if not should_retry or attempt == max_retries:
            return resp

        if retry_after:
            sleep_s = int(retry_after)
        elif remaining == "0" and reset:
            # Rate limit exhausted: sleep until reset (+1s safety)
            sleep_s = max(1, int(reset) - int(time.time()) + 1)
        else:
            # Exponential backoff + jitter
            base = 2 ** attempt
            sleep_s = min(60, base) + random.random()

        print(f"Retrying in {sleep_s:.1f}s (attempt {attempt+1}/{max_retries}) -> HTTP {resp.status_code}")
        time.sleep(sleep_s)

    return resp  # should not reach


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--per-page", type=int, default=50)
    ap.add_argument("--max-pages", type=int, default=2)
    args = ap.parse_args()

    session = requests.Session()
    url = args.url
    params = {"per_page": args.per_page}

    total = 0
    for page in range(1, args.max_pages + 1):
        params["page"] = page
        r = resilient_get(session, url, params=params)
        if r.status_code != 200:
            print(f"ERROR: HTTP {r.status_code}\n{r.text[:500]}")
            return 1

        data = r.json()
        if not isinstance(data, list):
            print("Non-list JSON response (showing keys):", list(data.keys()))
            return 1

        print(f"Page {page}: {len(data)} items")
        total += len(data)

        # Stop early if fewer than per_page came back
        if len(data) < args.per_page:
            break

    print("Total items:", total)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
