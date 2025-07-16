from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import FoodItemViewSet, NutritionLogViewSet

router = DefaultRouter()
router.register(r'food-items', FoodItemViewSet)
router.register(r'nutrition-logs', NutritionLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]