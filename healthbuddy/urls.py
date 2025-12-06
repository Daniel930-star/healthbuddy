"""
URL configuration for healthbuddy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
# from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('workouts/', include('workouts.urls')),
    path('nutrition/', include('nutrition.urls')),
    path('progress/', include('progress.urls')),
    path('water/', include('water.urls')),
    path('goals/', include('goals.urls')),
    path('', include('home.urls')),  # homepage will be at root
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from django.contrib import admin
# from django.urls import path, include
# from django.views.generic import TemplateView
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', TemplateView.as_view(template_name='home.html'), name='home'),  # Home page
#     path('workouts/', include('workouts.urls')),
#     path('progress/', include('progress.urls')),
#     path('nutrition/', include('nutrition.urls')),
#     path('goals/', include('goals.urls')),
#     path('water/', include('water.urls')),
#     path('users/', include('users.urls')),  # Users app
# ]
