from django.shortcuts import render
from .models import Product
from django.forms.models import model_to_dict
from django.http import JsonResponse
"""         Converting DJANGO to DRF         """
from rest_framework.response import Response
from rest_framework.decorators import api_view
"""          Model Serializers                """
from .serializers import ProductSerializer

# Create your views here.

@api_view(["GET"])
def api_product(request, *args, **kwargs):

    instance = Product.objects.all().order_by("?").first() # Returns Random Product from List
    data = {}

    if instance:
        """data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price """   

    # data = model_to_dict(model_data, fields=['title', 'price', 'sale_price']) # It will not return "sale_price"
    print(instance)
    data = ProductSerializer(instance).data # .data returns a list/dict
    return Response(data)

    # print(data)
    # data = dict(data)
    # json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers= {"content-type":"application/json"})
