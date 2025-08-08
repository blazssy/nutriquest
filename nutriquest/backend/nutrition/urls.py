from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import FoodItemViewSet, NutritionLogViewSet
from django.urls import path
from .views import suggest_meal_pairs


router = DefaultRouter()
router.register(r'food-items', FoodItemViewSet)
router.register(r'nutrition-logs', NutritionLogViewSet)
 

urlpatterns = [
    path('', include(router.urls)),
    path("suggest-meal-pairs/", suggest_meal_pairs,name='suggest-meal-pairs'),

]