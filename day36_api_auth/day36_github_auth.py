import os
import requests
from pathlib import Path
from datetime import datetime

#1) Read environment
env=os.environ.get("APP_ENV","dev").lower()
token=os.environ.get("GITHUB_TOKEN")

print(f"Running in {env} mode")

#2) setup logging
logs_dir=Path("logs")
logs_dir.mkdir(exist_ok=True)
log_file=logs_dir/"api_auth.log"

def log(msg: str) -> None:
    ts=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with log_file.open("a") as f:
        f.write(f"{ts}-{env}-{msg}\n")

#3) Token check
if not token:
    print("ERROR: GotHUB Token is missing")
    log("FAIL-Missing token(GITHUB_TOKEN not set)")
    raise SystemExit(1)

#4) Call Authentical endpoint
url="https://api.github.com/user"
headers={
    "Authorization":f"Bearer {token}",
    "Accept":"application/vnd.github+json"
}

try:
    response=requests.get(url, headers=headers,timeout=10)
    print("Status code: ",response.status_code)

    #Raise for 4xx/5xx
    response.raise_for_status()

    data=response.json()

    #5 Print 3-5 fields
    print("\nUser Info:")
    print("Login",data.get("login"))
    print("ID",data.get("id"))
    print("Public repos",data.get("public_repos"))
    print("Profile URL",data.get("html_url"))

except requests.exceptions.HTTPError as e:
    print("HTTP/Auth error: ",e)
    log(f"FAIL -HTTP error (status={response.status_code})")

except requests.exceptions.RequestException as e:
    print("Request failed:",e)
    log("FAIL-RequestException(network/timeout/etc.)")

else:
    print("\nLogged to logs/api_auth.log")









