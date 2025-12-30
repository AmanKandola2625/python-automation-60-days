# Day 37 — Pagination & Rate Limits (GitHub API)

## Goals
- Handle paginated API responses (page/per_page + Link headers)
- Respect rate limits and recover gracefully (429 / 403 secondary limits)
- Build a reusable `GET` helper with retries + exponential backoff

## Setup
Optional (recommended): create a GitHub token and set it as an env var:
- Windows PowerShell:
  $env:GITHUB_TOKEN="your_token_here"
- Git Bash:
  export GITHUB_TOKEN="your_token_here"

Install deps:
  pip install requests

## Run
1) Paginated fetch:
  python github_list_repos_paginated.py --user octocat --per-page 30 --max-pages 3

2) Rate limit status:
  python github_rate_limit_status.py

3) Resilient GET demo:
  python resilient_get.py --url https://api.github.com/users/octocat/repos --per-page 50 --max-pages 2
