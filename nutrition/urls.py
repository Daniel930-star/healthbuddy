# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.nutrition_home, name='nutrition_home'),
# ]
from django.urls import path
from . import views

app_name = 'nutrition'

urlpatterns = [
    path('', views.nutrition_list, name='nutrition_list'),
    path('edit/<int:pk>/', views.edit_nutrition, name='edit_nutrition'),
    path('delete/<int:pk>/', views.delete_nutrition, name='delete_nutrition'),
]
