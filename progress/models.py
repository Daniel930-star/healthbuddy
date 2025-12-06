from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.utils import timezone


User = settings.AUTH_USER_MODEL

class NutritionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nutrition_logs')
    meal = models.CharField(max_length=200)
    calories = models.PositiveIntegerField()
    date = models.DateField()  # date of the meal (not datetime)
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.meal} ({self.calories} kcal) on {self.date}"

class NutritionGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nutrition_goals')
    daily_calorie_target = models.PositiveIntegerField(help_text="Target calories per day")
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.daily_calorie_target} kcal/day ({'active' if self.active else 'inactive'})"

class ProgressPhoto(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='progress_photos')
    photo = models.ImageField(upload_to='progress_photos/')
    date = models.DateField(default=timezone.now)
    notes = models.TextField(blank=True, null=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-uploaded_at']

    def __str__(self):
        return f"Photo {self.date} ({self.user.username})"