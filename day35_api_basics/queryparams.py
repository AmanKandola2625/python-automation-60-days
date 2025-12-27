import requests
params={"q": "python","sort":"stars"}
response=requests.get("https://api.github.com/search/repositories",params=params)

data=response.json()
print("Total repos found:",data["total_count"])
