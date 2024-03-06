from django.urls import path
from . import views

urlpatterns = [
    path('knn/', views.predictor, name='predictor'),
    path('result', views.formInfo, name='result'),
    path('knn/result', views.formInfo, name='result'),
]