from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    my_discount = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Product
        fields = [
            'id', 
            'title', 
            'content', 
            'price', 
            ## 'get_discount', we will be calling it as discount as follows
            'my_discount',
        ]

    def get_my_discount(self,obj):
            print(obj)
            return obj.get_discount()
