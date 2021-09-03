from django_filters import rest_framework as filters
from .models import Orders
from django_filters import DateTimeFilter, IsoDateTimeFilter
from django.db import models as django_models


class FilterOrderDate(filters.FilterSet):
    IsoDateTimeFilter(field_name='created_at', lookup_expr='gte')
    IsoDateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Orders
        fields = {
            'created_at': ('gte', 'lte')
        }
