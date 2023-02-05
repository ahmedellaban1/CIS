from rest_framework import generics
from products.serializers import ProductSerializer
from products.models import Product

class Search(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        user = None
        result = Product.objects.none()
        if q is not None:
            if self.request.user is not None or self.request.user.is_authenticated:
                user = self.request.user
                result = qs.search(q, user=user)
        return result