from django.http import JsonResponse
from rest_framework import viewsets
from .models import FoodItem, NutritionLog
from .serializers import FoodItemSerializer, NutritionLogSerializer

# Helper to serialize a single FoodItem instance to a dict
def item_to_dict(item):
    return {
        "id": item.id,
        "name": item.name,
        "calories": item.calories,
        "protein": item.protein,
        "carbs": item.carbs,
        "fat": item.fat,
    }

# Helper to serialize a pair of FoodItem instances
def pair_to_dict(pair):
    first, second = pair
    return {
        "first": item_to_dict(first),
        "second": item_to_dict(second),
        "total_calories": first.calories + second.calories
    }

class FoodItemViewSet(viewsets.ModelViewSet):
    """
    Provides list, retrieve, create, update, destroy for FoodItem.
    """
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class NutritionLogViewSet(viewsets.ModelViewSet):
    """
    Provides list, retrieve, create, update, destroy for NutritionLog.
    """
    queryset = NutritionLog.objects.all()
    serializer_class = NutritionLogSerializer

def suggest_meal_pairs(request):
    """
    GET /api/suggest-meal-pairs/?target=XXX[&filter=high-protein|low-carb|balanced]
    Returns JSON with pairs of FoodItems matching the target ±50 calories,
    optionally filtered by macro criteria.
    """
    target = int(request.GET.get("target", 0))
    filter_type = request.GET.get("filter", "")

    items = list(FoodItem.objects.all())
    pairs = []

    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            a, b = items[i], items[j]
            total = a.calories + b.calories

            if abs(total - target) > 50:
                continue

            # Macro filters
            if filter_type == "high-protein":
                if (a.protein + b.protein) < 20:
                    continue

            elif filter_type == "low-carb":
                if (a.carbs + b.carbs) > 30:
                    continue

            elif filter_type == "balanced":
                p, c, f = a.protein + b.protein, a.carbs + b.carbs, a.fat + b.fat
                # crude ratio check
                if not (0.8 < p/c < 1.2 and 0.8 < p/f < 1.2):
                    continue

            pairs.append((a, b))

    # Return serialized pairs
    return JsonResponse({"pairs": [pair_to_dict(p) for p in pairs]})