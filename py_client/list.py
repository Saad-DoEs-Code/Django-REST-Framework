import requests

auth_endpoint = "http://127.0.0.1:8000/auth/"
auth_response = requests.post(auth_endpoint, json={"username":"saad", "password":"1234"})
# print(response.json())
# token = response.json()['token']

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://127.0.0.1:8000/api/product/list"
    response = requests.get(endpoint, headers=headers)
    print(response.json())