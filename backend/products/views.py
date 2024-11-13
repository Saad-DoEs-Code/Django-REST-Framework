from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product


class ProductsDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_fieled = 'pk'















# from django.shortcuts import render
# from .models import Product
# from django.forms.models import model_to_dict
# from django.http import JsonResponse, HttpResponse
# """         Converting DJANGO to DRF         """
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# """          Model Serializers                """
# from .serializers import ProductSerializer

# # Create your views here.

# @api_view(["GET"])
# def api_get(request, *args, **kwargs):

#     instance = Product.objects.all().order_by("?").first() # Returns Random Product from List
#     data = {}

#     if instance:
#         """data['id'] = model_data.id
#         data['title'] = model_data.title
#         data['content'] = model_data.content
#         data['price'] = model_data.price """   

#     # data = model_to_dict(model_data, fields=['title', 'price', 'sale_price']) # It will not return "sale_price"
#     print(instance)
#     data = ProductSerializer(instance).data # .data returns a list/dict
#     return Response(data)

#     # print(data)
#     # data = dict(data)
#     # json_data_str = json.dumps(data)
#     # return HttpResponse(json_data_str, headers= {"content-type":"application/json"})

# @api_view(["POST"]) # It will manage the CSRF Token as it is done manually in DJANGO. 
# def api_post(request, *args, **kwargs):

#     # The request will contain the data posted through the client
#     # data = request.data
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         instance = serializer.save()
#         print(instance)
#         return Response(serializer.data)
#     return Response(serializer.errors, status=400)