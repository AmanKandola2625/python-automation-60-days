import requests
headers={"Accept": "application/vnd.github+json"}

response=requests.get("https://api.github.com",headers=headers)
print(response.status_code)
