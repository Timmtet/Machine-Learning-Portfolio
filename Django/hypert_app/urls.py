from django.urls import path
from . import views

urlpatterns = [
    path('log/', views.predictor, name='predictor'),
    path('result', views.formInfo, name='result'),
    path('log/result', views.formInfo, name='result'),
]