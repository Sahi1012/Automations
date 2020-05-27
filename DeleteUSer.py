import requests
import json
import jsonpath
url = "https://reqres.in/api/users/2"
delete_user = requests.delete(url)
print(delete_user)