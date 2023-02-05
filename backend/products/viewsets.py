from rest_framework import viewsets, mixins
from .models import Product
from .serializers import ProductSerializer

class ProductViewset(viewsets.ModelViewSet):
    '''
        get --> list --> Queryset
        get --> retrieve --> object instance view detail
        post --> create --> create new object
        put --> update --> edit specific object
        patch --> partial update --> edit specific object
        delete --> destroy --> delete specific object
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'



class ProductGenericViewset(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    '''
        get --> list --> Queryset
        get --> retrieve --> object instance view detail
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


