from logging import raiseExceptions
from pickle import PUT
from django.shortcuts import get_object_or_404
from http.client import FOUND
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from products import serializers

# Create your views here.
@api_view(["GET", 'POST'])
def product_list(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


'''@api_view(["GET", 'PUT'])
def single_product(request, pk):
    if request == 'GET':
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request == 'PUT':'''
