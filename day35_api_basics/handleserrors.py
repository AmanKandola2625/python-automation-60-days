import requests
url="https://api.github.com/invalid"

try:
    response=requests.get(url,timeout=5)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.HTTPError as e:
    print("HTTP error: ",e)
except requests.exceptions.RequestException as e:
    print("Request failed",e)
