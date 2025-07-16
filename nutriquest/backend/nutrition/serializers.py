from rest_framework import serializers
from .models import FoodItem, NutritionLog

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model  = FoodItem
        fields = '__all__'

class NutritionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model  = NutritionLog
        fields = '__all__'