import  jsonpath
import json
import  requests

url = "https://reqres.in/api/users/2"
file = open(r"D:\Notes\JsonTest" , 'r')
read=file.read()
json_request = requests.put(url,read)
assert json_request.status_code ==200

json_loads = json.loads(json_request.text)
json_path = jsonpath.jsonpath(json_loads,"updateAt")
print(json_path)