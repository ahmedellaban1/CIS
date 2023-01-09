import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/" 
# i can send params in endpoint like http://127.0.0.1:8000/api/?abc=123
# get_response = requests.get(endpoint,params={"abc":123} ,json={"query":"hello world"}) 
get_response = requests.post(endpoint,json={"title":None}) 
# print(get_response.headers)
print(get_response.text) # returned data in JSON format to string format
# HTTP Request return with HTML document
# REST API HTTP Request return with JSON 
# JSON == ' JavaScript Object Notation ' ~> ' python dictionary ' 
# print(get_response.json()) # returned data in python dictionary format
print(get_response.status_code)