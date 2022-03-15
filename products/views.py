from logging import raiseExceptions
from django.shortcuts import get_object_or_404
from http.client import FOUND
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from products import serializers

# Create your views here.
@api_view(["GET"])
def product_list(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)

    return Response("serializer")