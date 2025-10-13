import requests
import os
from PIL import Image
from IPython.display import IFrame

url = 'https://www.ibm.com/'
r = requests.get(url)

print(r.status_code)
print(r.request.headers)
print("request body: ", r.request.body)

header = r.headers
print(r.headers)

print(header['Date'])

print(header['Content-Type'])

print(r.encoding)

print(r.text[0:100])

# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

r = requests.get(url)

print(r.headers)

print(r.headers['Content-Type'])

path = os.path.join(os.getcwd(), 'image.png')

with open(path, 'wb') as f:
    f.write(r.content)

print(Image.open(path))

# download a file
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path = os.path.join(os.getcwd(),'example1.txt')
r = requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)

url_get = 'http://httpbin.org/get'
payload = {"name": "Joseph", "ID": "123"}
r = requests.get(url_get, payload)
print(r.url)
print("request body: ", r.request.body)
print(r.status_code)
print(r.text)
print(r.headers['Content-Type'])
print(r.json())
print(r.json()['args'])

url_post = 'http://httpbin.org/post'
r_post = requests.post(url_post, data=payload)
print("POST request URL: ", r_post.url)
print("GET request URL: ", r.url)
print("POST request URL: ", r_post.url) # Use r_post instead of respond
print("POST request body: ", r_post.request.body)
print("GET request body: ", r.request.body)
print(r_post.json()['form']) 





