from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class NutritionLog(models.Model):
    MEAL_TYPES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)
    food_name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.food_name} ({self.calories} kcal)"
