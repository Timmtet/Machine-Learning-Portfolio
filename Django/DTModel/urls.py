
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('a_urinaryApp.urls')),
    path('', include('irish_app.urls')) ,
    path('', include('drugs_app.urls')) ,
    path('', include('titanic.urls')) ,
    path('', include('milk_app.urls')) ,
    path('', include('hypert_app.urls')) ,
    path('', include('housing_app.urls')) ,
    path('admin/', admin.site.urls),
]
