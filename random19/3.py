import requests

response=requests.get("https://en.wikipedia.org/robots.txt")

print(response.text)