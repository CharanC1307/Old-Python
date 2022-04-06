import requests

url="https://www.w3schools.com/howto/tryhow_make_a_website.htm"

response=requests.get(url)

print(f"Status Code: {response.status_code}")
print(response.text)