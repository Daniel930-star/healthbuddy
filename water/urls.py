from django.urls import path
from . import views


app_name = 'water'
urlpatterns = [
    path('', views.water_home, name='water_home'),
    path('', views.water_home, name='water_home'),
    path('add-log/', views.add_log, name='add_log'),
    path('edit-log/<int:pk>/', views.edit_log, name='edit_log'),
    path('delete-log/<int:pk>/', views.delete_log, name='delete_log'),
    path('add-goal/', views.add_goal, name='add_goal'),
    path('', views.log_list, name='log_list'),
]

