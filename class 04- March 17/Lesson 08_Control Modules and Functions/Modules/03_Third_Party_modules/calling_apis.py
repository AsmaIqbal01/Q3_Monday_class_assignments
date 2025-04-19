import requests #for making HTTP requests (like calling APIs)
response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json()["current_user_url"])                       