
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('a_urinaryApp.urls')),
    path('admin/', admin.site.urls),
]
