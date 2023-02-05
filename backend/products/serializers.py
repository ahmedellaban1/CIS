from rest_framework import serializers
from rest_framework.reverse import reverse
from products.models import Product
from . import validator
from api.serializers import UserPublicSerializer

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user',read_only=True)
    my_user_data = serializers.SerializerMethodField(read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)

    # get urls for views classes or functions
    url_detail = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    url_edit = serializers.SerializerMethodField(read_only=True)
    url_delete = serializers.SerializerMethodField(read_only=True)
    url_hyper_link = serializers.HyperlinkedIdentityField(
        view_name='product-delete',
        lookup_field = 'pk'
    )
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators = [# override title field and apply property on it
        validator.validate_title_no_hello,
        validator.unique_product_title]) # unique not working of no field called hello in database
    # name = serializers.CharField(source='title', read_only=True) # another way to override specific field
    class Meta:
        model = Product
        fields = [
            'owner', 
            'url',
            'url_hyper_link',
            'url_edit',
            'url_detail',
            'url_delete',
            # 'email',
            'pk',
            'title',
            # 'name',
            'content',
            'price',
            'sale_price',
            'my_discount',
            'public',
            'my_user_data',

        ]

        # -----------------------------------------------------
    def get_my_user_data(self, obj):
        response = {
            "username":obj.user.username,
            "di":obj.user.id,
        }
        return response
    def get_url(self, obj):
        # return f"api/products/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-list", request=request)

        # -----------------------------------------------------

    def get_url_edit(self, obj):
        # return f"api/products/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-put", kwargs={"pk":obj.pk},request=request)

        # -----------------------------------------------------

    def get_url_detail(self, obj):
        # return f"api/products/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detial",kwargs={"pk":obj.pk}, request=request)

        # -----------------------------------------------------

    def get_url_delete(self, obj):
        # return f"api/products/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-delete",kwargs={"pk":obj.pk}, request=request)

        # ----------------------------------------------------- 

    # this function dosn't work if there is no instance created from this serializer
    def get_my_discount(self, obj): # obj = instance that called from serializer 
        # print(obj.title or .id or .etc)
        if not hasattr(obj, 'id'): # id ????
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()

        # -----------------------------------------------------

    # def create(self, validated_data):
    #     email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     return obj

    # the next method use if i want to create an object with an unique data in specific model field
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already product name ")
    #     return value