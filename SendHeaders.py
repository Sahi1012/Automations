import  requests

headerData = {'T1':'First Header', 'T2' : 'Second Header'}
response = requests.get( url='https://httpbin.org/get' , headers= headerData)
print(response.text)

'''from selenium.webdriver  import Chrome

path="Path of Webdriver exe"

driver = Chrome(executable_path=path)

driver.get('http://www.thetestingworld.com/testings')'''