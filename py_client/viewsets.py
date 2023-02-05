import requests
endpoint = 'http://127.0.0.1:8000/api/v2/products-abc/'
json = {
        "title": "hello world",
}
getresponse = requests.post(endpoint,json=json)
