from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class WaterLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='water_logs')
    amount_ml = models.PositiveIntegerField(help_text="Amount of water in ml")
    date = models.DateField(default=timezone.now)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.amount_ml} ml on {self.date}"

class WaterGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='water_goals')
    daily_target_ml = models.PositiveIntegerField(help_text="Daily water target in ml")
    active = models.BooleanField(default=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.daily_target_ml} ml/day ({'active' if self.active else 'inactive'})"
