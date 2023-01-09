from rest_framework import authentication,generics, mixins, permissions
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404 # instead of except  error 404 this function is prepared for dealing with it
from .permissions import IsStaffEditorPermission
from api.authentication import TokenAuthentication

class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication
        # authentication.TokenAuthentication,   # overridden
    ]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    # 1:39:00 <--------------------------------------

product_list_create_api_view = ProductListCreateApiView.as_view()


class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

product_detail_api_view = ProductDetailApiView.as_view()


class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.DjangoModelPermissions]
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.tite

product_update_api_view = ProductUpdateApiView.as_view()



class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_distroy(self, instance):
        super().perform_destroy(instance)
        
product_distroy_api_view = ProductDestroyAPIView.as_view()


# class ProductListApiView(generics.ListAPIView):
#     """
#        not gonna use this method 
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
# product_list_api_view = ProductListApiView.as_view()

class ProductMixinVeiw(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(args, kwargs)
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = "this a single view doing cool stup"
        serializer.save(content=content)
        
product_mixin_view = ProductMixinVeiw().as_view()
    

@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None,*args, **kwargs):
    method = request.method
    if method == "GET":
        if pk != None:
            # detail view == if i want to get specific item from database
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data # === > serializer.data
            return Response(data)
        # else: can be written but i returned response in if and if it no response else will run auto
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
            
    if method == "POST":
        pass
        # create an item 
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title') # type: ignore
            content = serializer.validated_data.get('content') or None # type:ignore
            if content is None:
                content = title
            instance = serializer.save(content=content)
            print(serializer.data)
            return Response(serializer.data)
        return Response({"message":" invalid data "},status=400)