from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, OrderViewSet, ClientViewSet, CarViewSet


router = DefaultRouter()
router.register('users', UserViewSet)
router.register('orders', OrderViewSet)
router.register('clients', ClientViewSet)
router.register('cars', CarViewSet)


urlpatterns = [
    path('', include(router.urls)),
]