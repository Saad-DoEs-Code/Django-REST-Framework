import requests

endpoint = "http://127.0.0.1:8000/api/product/7222/delete/"
response = requests.delete(endpoint)
print(response.status_code, response.status_code == 204)