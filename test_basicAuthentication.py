import requests
from requests.auth import HTTPBasicAuth

def test_with_authentication():
    response = requests.get("https://api.github.com/user", auth= HTTPBasicAuth('Sahi1012','Sahi@1992'))
    print(response.text)
    print(response.content)

