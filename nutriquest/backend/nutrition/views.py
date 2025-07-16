from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import FoodItem, NutritionLog
from .serializers import FoodItemSerializer, NutritionLogSerializer

class FoodItemViewSet(viewsets.ModelViewSet):
    queryset         = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class NutritionLogViewSet(viewsets.ModelViewSet):
    queryset         = NutritionLog.objects.all()
    serializer_class = NutritionLogSerializer