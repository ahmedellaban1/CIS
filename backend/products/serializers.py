from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]
    # this function dosn't work if there is no instance created from this serializer
    def get_my_discount(self, obj): # obj = instance that called from serializer 
        # print(obj.title or .id or .etc)
        if not hasattr(obj, 'id'): # id ????
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()