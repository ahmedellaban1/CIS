import requests
headers = {'Authorization': 'Bearer 38a3bb27f93ad7d66b418322b22c22be18ec98c2'}

endpoint = "http://127.0.0.1:8000/api/products/"
data = {
    "title":"done",
} 
get_response = requests.post(endpoint,json=data, headers=headers) 
print(get_response.text)
print(get_response.json())
print(get_response.status_code)