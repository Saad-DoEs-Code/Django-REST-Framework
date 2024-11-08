from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):

    # print(request.GET) # Returns URL params
    body = request.body
    data = {}
    # This Try/Except Block is necessary as it can get an empty JSON Data
    try:
        data = json.loads(body) # Converts JSON Data into PYTHON Dictionary
    except:
        pass

    # We can add DATA to our "data" variable
    data['headers'] = dict(request.headers)
    data['method'] = request.method
    data['content_type'] = request.content_type
    data['params'] = dict(request.GET)    
    # print(data.keys())

    return JsonResponse(data)