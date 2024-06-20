from .serializers import *
from .models import *
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .filter import ProductFilter
from rest_framework.filters import SearchFilter


class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['product_name']
    permission_classes = [permissions.IsAuthenticated]

