from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Cars, Orders, Users, Clients
from .serializers import CarSerializer, OrderSerializer, UserSerializer, ClientSerializer
from .filters import FilterOrderDate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class CarViewSet(ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer

### Сколько раз определенная машина встречается в ордере ###
    @action(detail=True, methods=['GET'])
    def orders(self, request, *args, **kwargs):
        car = self.get_object()
        serializer = OrderSerializer(car.orders_set.all(), many=True)
        return Response(serializer.data)

class OrderViewSet(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['created_at']
    filter_class = FilterOrderDate


class UserViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class ClientViewSet(ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer


