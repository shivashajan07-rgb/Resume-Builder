from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    # Add this line to include Django's built-in auth URLs
    path('', include('django.contrib.auth.urls')),
]