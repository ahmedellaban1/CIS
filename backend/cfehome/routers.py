from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewset, ProductGenericViewset

router = DefaultRouter()
router.register('products', ProductViewset, basename='products')
router.register('products-v2', ProductGenericViewset, basename='products-v2')

urlpatterns = router.urls