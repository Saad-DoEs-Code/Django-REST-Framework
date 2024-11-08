from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
import json

# Create your views here.


def api_product(request, *args, **kwargs):

    model_data = Product.objects.all().order_by("?").first() # Returns Random Product from List
    
    data = {}

    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price    
    
    return JsonResponse(data)
