import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"
get_response = requests.get(endpoint)
#print(get_response) # Returns Status Code
#print(get_response.text) # Returns Text/Raw Text of HTML Page Structure

#print(get_response.json()) # Returns the JSON Data in the form of Python Object
#print(get_response.json()['message']) # Returns the Value against the specified Key

"""         ECHOING DATA BACK TO BACKEND        """
# get_response = requests.get(endpoint, params={"abc":123}, json={"message":"Hello World"}) 
# print(get_response.json())

"""         CALLING DATA FROM PRODUCT MODELS        """
# endpoint = "http://127.0.0.1:8000/product/get"
# get_response = requests.get(endpoint) 
# print(get_response.json())
# print("yes")

"""         POSTING DATA TO MODELS"         """
endpoint = "http://127.0.0.1:8000/product/post"
post_request = requests.post(endpoint,json={"title":"Iphone 13", "price":200000})
print(post_request.json())
