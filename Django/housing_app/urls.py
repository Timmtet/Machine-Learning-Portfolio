from django.urls import path
from . import views

urlpatterns = [
    path('lin/', views.predictor, name='predictor'),
    path('result', views.formInfo, name='result'),
    path('lin/result', views.formInfo, name='result'),
]