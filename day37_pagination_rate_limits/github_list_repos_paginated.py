-import argparse
import os
import re
import sys
import time
from typing import Dict,Iterator,Optional,Tuple

import requests

def build_headers() ->Dict[str,str]:
    headers={
        "Accept": "application/vnd.github+json",
        "User-Agent":"python-automation-60-days-day37",
    }
    token=os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorizaion"]=f"Bearer {token}"
    return headers

_link_re=re.compile(r'<([^>]+)>;\s*rel="([^"]+)"')

def parse_link_header(link_header: str)->Dict[str, str]:
    links: Dict[str, str] = {}
    for part in link_header.split(","):
        part = part.strip()
        m = _link_re.search(part)
        if m:
            url, rel = m.group(1), m.group(2)
            links[rel] = url
    return links

def iter_pages(
    url: str,
    params: Dict[str,str],
    max_pages: Optional[int] = None
) ->Iterator[Tuple[requests.Response,int]]:
    session = requests.Session()
    headers = build_headers()


    page = 1
    next_url = url
    next_params = params.copy()

    while True:
        resp = session.get(
            next_url,
            headers = headers,
            params=next_params,
            timeout=30
        )
        yield resp, page

        if max_pages is not None and page >=max_pages:
            return
        link = resp.headers.get("Link","")
        if not link:
            return

        links = parse_link_header(link)
        if "next" not in links:
            return
        next_url=links["next"]
        next_params={}
        page+=1

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", required=True)
    ap.add_argument("--per-page", type=int, default=30)
    ap.add_argument("--max-pages", type=int, default=3)
    args = ap.parse_args()

    url = f"https://api.github.com/users/{args.user}/repos"
    params = {"per_page": str(args.per_page), "sort": "updated"}

    total = 0
    for resp, page in iter_pages(url, params, max_pages=args.max_pages):
        if resp.status_code != 200:
            print(f"ERROR: HTTP {resp.status_code} on page {page}")
            print(resp.text[:500])
            return 1

        repos = resp.json()
        print(f"\nPage {page}: {len(repos)} repos")
        for r in repos:
            total += 1
            print(f"- {r.get('full_name')}  (updated: {r.get('updated_at')})")

        time.sleep(0.25)

    print(f"\nTotal repos listed: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())









        






















    
