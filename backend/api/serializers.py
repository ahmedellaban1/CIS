from rest_framework import serializers

class UserProductInlineSerializer(serializers.Serializer):
    url_hyper_link = serializers.HyperlinkedIdentityField(
        view_name='product-delete',
        lookup_field = 'pk',
        read_only=True,
    )
    title = serializers.CharField(read_only=True)
    content = serializers.CharField(read_only=True)


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    
    # email = serializers.EmailField(read_only=True)
    # other_product = serializers.SerializerMethodField(read_only=True)

    # def get_other_product(self, obj):
    #     # obj is the instance that created from this serializer 
    #     user = obj # i can use user directly as a parameter return by instance data but this for illustrate
    #     user_product_qs = user.product_set.all()[:5]
    #     print(user_product_qs)

    #     return UserProductInlineSerializer(user_product_qs, many=True, context=self.context).data
