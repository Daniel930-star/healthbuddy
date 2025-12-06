from django.urls import path
from . import views
app_name = 'goals'

urlpatterns = [
    path('', views.goals_home, name='goals_home'),
# Goals
    path('goals/', views.goals_home, name='goals_home'),
    path('add/', views.add_goal, name='add_goal'),
    path('add-goal/', views.add_goal, name='add_goal'),
    path('edit-goal/<int:pk>/', views.edit_goal, name='edit_goal'),
    path('delete-goal/<int:pk>/', views.delete_goal, name='delete_goal'),

]
