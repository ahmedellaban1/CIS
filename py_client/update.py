import requests

endpoint = "http://127.0.0.1:8000/api/products/1/update/" 
data = {
    "title":"hello world",
    "content":"content content",
    "price":55.55,

}
get_response = requests.put(endpoint,json=data) 
print(get_response.text)
print(get_response.status_code)