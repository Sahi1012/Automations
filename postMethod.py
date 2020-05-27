import  requests
import json
import  jsonpath

file = open(r"D:\Notes\JsonTest" ,'r')
json_input = file.read()
json_loads = json.loads(json_input)


url = "https://reqres.in/api/users"
response = requests.post(url , json_loads)

assert  response.status_code == 201

url_data = json.loads(response.text)
json_path = jsonpath.jsonpath(url_data , 'name')
print(json_path)