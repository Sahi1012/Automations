import json
import requests
import jsonpath

url = "https://reqres.in/api/users?page=2"
get= requests.get(url)

#print(get)

#Display Response Content
#print(get.content)
#print(get.headers)


#Validate Response Code
response_code = get.status_code
assert  response_code == 200
print(get.headers.get('Date'))
print(get.headers.get('Connection'))
print(get.encoding)
#Fetch Everything in a Text Format
response = json.loads(get.text)
print(response)
#Search required data with JsonPath

for i in range(0,3):
    data = jsonpath.jsonpath(response,'data['+str(i)+'].first_name')
    print(data)
