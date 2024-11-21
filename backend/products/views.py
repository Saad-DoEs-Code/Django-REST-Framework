from rest_framework import generics,mixins,permissions, authentication
from .serializers import ProductSerializer
from .models import Product


"""FOR FUNCTION BASED VIEW - LINE 39"""
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

"""PERMISSIONS AND AUTHENTICATION"""

from api.mixins import StaffPermissionsMixin
from api.authentication import TokenAuthentication


class ProductsDetailView(StaffPermissionsMixin,generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_fieled = 'pk'


class ProductsListCreateView(StaffPermissionsMixin,generics.ListCreateAPIView):
    """Takes
    GET Method: to list all the objects from DB,
    POST Method: to create a new object
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [TokenAuthentication, authentication.SessionAuthentication] Commented due to Default defined in REST_FRAMEWORK in settings.py
    # permission_classes = [permissions.IsAdminUser,IsStaffPermissions]


class ProductCreateAPIView(StaffPermissionsMixin,generics.CreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        price = serializer.validated_data.get("price")
        content = serializer.validated_data.get('content') or None
        if content == None:
            content = "No content"
            # price = 0
            serializer.save(content=content)

class ProductUpdateView(StaffPermissionsMixin,generics.UpdateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = "No content"
    
class ProductDeleteView(StaffPermissionsMixin,generics.DestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    
    
"""Function Based View to Create or Retrieve List View"""

class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    StaffPermissionsMixin,
    generics.GenericAPIView):

    # ListModelMixin allows us to declare queryset, serializer_class
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # The lookup_field works with RetrieceAPIView(detail view)
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        
        pk = kwargs.get("pk")
        if pk is not None:
            print(args)
            print(kwargs)
            return self.retrieve(request, *args, **kwargs)
        print(args)
        print(kwargs)
        return self.list(request,*args,**kwargs)
    
    def post(self, request, *args, **kwargs):
        print(request.body)
        return self.create(request,*args, **kwargs)
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        price = serializer.validated_data.get("price")
        content = serializer.validated_data.get('content') or None
        if content == None:
            content = "Created with mixin"
            # price = 0
            serializer.save(content=content)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


@api_view(["GET", "POST"])
def get_or_post_product(request, pk=None, *args, **kwargs):

    if request.method == "GET":
        if pk is not None:
            # detail view
            product = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(product).data
            return Response(data)
        else:
            # list view
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
            data = serializer.data
            return Response(data)

    if request.method == "POST":
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

# product_alt_view = get_or_post_product()

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
