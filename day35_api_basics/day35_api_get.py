import requests
url="https://api.github.com"
response=requests.get(url)

print("Status Code: ",response.status_code)
print("Headers: ",response.headers)
print("JSON: ",response.json())
