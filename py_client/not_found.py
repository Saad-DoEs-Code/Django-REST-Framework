import requests

endpoint = "http://127.0.0.1:8000/api/product/35624"
response = requests.get(endpoint)
print(response.json())