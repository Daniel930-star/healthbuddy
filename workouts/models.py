from django.db import models

class Workout(models.Model):
    title = models.CharField(max_length=200, default='Untitled Workout')
    details = models.TextField(default='No details provided.')
    duration = models.IntegerField(default=0)  # duration in minutes
    workout_datetime = models.DateTimeField(null=True, blank=True)  # new field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
