from django.urls import path, include
from . import views

app_name = 'progress'

urlpatterns = [
    # Main dashboard
    path('', views.progress_home, name='progress_home'),

    # Nutrition Logs
    path('logs/add/', views.add_log, name='add_log'),
    path('logs/edit/<int:pk>/', views.edit_log, name='edit_log'),
    path('logs/delete/<int:pk>/', views.delete_log, name='delete_log'),

    # Goals
    path('goals/add/', views.add_goal, name='add_goal'),
    path('goals/edit/<int:pk>/', views.edit_goal, name='edit_goal'),
    path('goals/delete/<int:pk>/', views.delete_goal, name='delete_goal'),
    path('goals/', include('goals.urls')),

    # Progress Photos
    path('photos/add/', views.add_photo, name='add_photo'),
    path('photos/delete/<int:pk>/', views.delete_photo, name='delete_photo'),
]
