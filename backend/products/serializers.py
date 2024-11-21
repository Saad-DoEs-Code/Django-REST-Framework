from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse

class ProductSerializer(serializers.ModelSerializer):

    my_discount = serializers.SerializerMethodField(read_only = True)
    
    edit_url = serializers.HyperlinkedIdentityField(
        view_name='product-edit',
        lookup_field='pk',
        read_only=True
    )
    class Meta:
        model = Product
        fields = [
            'url',
            'edit_url',
            'id', 
            'title', 
            'content', 
            'price', 
            ## 'get_discount', we will be calling it as discount as follows
            'my_discount',
        ]
    """WAY 1 To GET ROUTE"""    
    url = serializers.SerializerMethodField(read_only = True)
    def get_url(self, obj):

        request = self.context.get("request")
        if request is None:
            return None
        return reverse('product-detail', kwargs={"pk":obj.pk}, request=request)
    
    # def get_url(self, obj):
    #     return f"api/v2/{obj.pk}/"

    def get_my_discount(self,obj):
        """We assume, an object instance if the serializer is attached to the model"""
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj,Product):
            return None
        return obj.get_discount()