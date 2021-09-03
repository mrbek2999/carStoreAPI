from rest_framework import serializers
from .models import Clients, Cars, Orders, Users


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('id', 'passport_series', 'firstname', 'lastname', 'phone')


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('id', 'brand', 'model')


class OrderSerializer(serializers.ModelSerializer):
    client_id = ClientSerializer()
    car_id = CarSerializer()
    class Meta:
        model = Orders
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'password')
