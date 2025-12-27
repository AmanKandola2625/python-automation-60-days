#Calls a public API (GitHub or similar)
#Prints status code
#Displays 3–5 fields from the JSON response
#Handles HTTP errors cleanly
#Saves a short summary to logs/api.log

import requests
from pathlib import Path
from datetime import datetime

#API endpoint
url="https://api.github.com"

#Log setup
logs_dir=Path("logs")
logs_dir.mkdir(exist_ok=True)
log_file=logs_dir/"api.log"

try:
    response=requests.get(url,timeout=5)

    #Print status code
    print("Status Code: ",response.status_code)

    #Raise error for bad status codes
    response.raise_for_status()

    data=response.json()

    #Display selected fields from JSON
    print("\nAPI Details")
    print("Current User URL",data.get("current_user_url"))
    print("Authoriztions URL",data.get("authorizations_url"))
    print("Repository search URL",data.get("repository_search_url"))
    print("Rate limit URL",data.get("rate_limit_url"))

    #Log summary
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with log_file.open("a") as f:
        f.write(f"{timestamp}-GitHub API reachable(Status {response.status_code})\n")
except requests.exceptions.HTTPError as e:
    print("HTTP error occured: ",e)

except requests.exceptions.RequestException as e:
    print("Request failed",e)

else:
    print("\nSummary saved to logs/api.log")
