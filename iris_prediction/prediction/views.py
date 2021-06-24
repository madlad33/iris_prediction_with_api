from django.shortcuts import render
from rest_framework import views, generics
from .serializers import FlowerSerializer
from .models import Flower


# Create your views here.

class FlowerPredictView(generics.ListCreateAPIView):
    """Simple Create and List View"""
    serializer_class = FlowerSerializer
    queryset = Flower.objects.all()



