import requests
data = {
    "title":"sameer ahmad",
    "price":200,
    # "content":"Harami"
}
endpoint = "http://127.0.0.1:8000/api/product/"
response = requests.post(endpoint, json=data)
print(response.json())