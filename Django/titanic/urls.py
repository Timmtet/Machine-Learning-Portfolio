from django.urls import path
from . import views

urlpatterns = [
    path('rfm/', views.predictor, name='predictor'),
    path('result', views.formInfo, name='result'),
    path('rfm/result', views.formInfo, name='result'),
]