from django.urls import path, include

from rest_framework.routers import DefaultRouter

from logistic import admin
from logistic.views import ProductViewSet, StockViewSet

router = DefaultRouter()

router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = router.urls
