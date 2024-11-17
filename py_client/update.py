import requests

endpoint = "http://127.0.0.1:8000/api/product/1/update/"
data = {
    "title":"Samsung S22 Ultra",
    "price": 120000,

}
response = requests.put(endpoint, json=data)
print(response.json())