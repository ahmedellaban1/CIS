from rest_framework.routers import DefaultRouter
from .viewsets import HerafiViewSetsAPIView, PreferredHerafi

router = DefaultRouter()
router.register('info', HerafiViewSetsAPIView, basename='herafi-information')
router.register('preferred-herafi', PreferredHerafi, basename='preferred-herafi')
urlpatterns = router.urls
