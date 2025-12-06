from django.urls import path
from . import views

app_name = 'workouts'

urlpatterns = [
    # List all workouts (home page for workouts)
    path('', views.workouts_list, name='workouts_list'),


    # Add a new workout
    path('add/', views.add_workout, name='add_workout'),

    # Edit an existing workout
path('edit/<int:workout_id>/', views.edit_workout, name='edit_workout'),

    # Update workout (alternative POST route if needed)
    path('update/<int:pk>/', views.update_workout, name='update_workout'),

    # Delete a workout
    path('delete/<int:pk>/', views.delete_workout, name='delete_workout'),

    # Workout history
    path('history/', views.workout_history, name='workout_history'),
]
