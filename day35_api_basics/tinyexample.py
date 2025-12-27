import requests

r = requests.get("https://api.github.com")
print(type(r.status_code))   # <class 'int'>
print(r.status_code)         # 200

