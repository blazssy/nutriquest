from django.db import models
from django.conf import settings

class FoodItem(models.Model):
    name      = models.CharField(max_length=100)
    calories  = models.PositiveIntegerField()
    image     = models.ImageField(upload_to='foods/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.calories} cal)"

class NutritionLog(models.Model):
    user      = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='logs'
    )
    food_item = models.ForeignKey(
        FoodItem,
        on_delete=models.CASCADE,
        related_name='logs'
    )
    quantity  = models.FloatField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.user} ate {self.quantity}×{self.food_item.name}"