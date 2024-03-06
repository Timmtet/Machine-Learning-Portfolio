from django.urls import path
from . import views

urlpatterns = [
    path('nbm/', views.predictor, name='predictor'),
    path('result', views.formInfo, name='result'),
    path('nbm/result', views.formInfo, name='result'),
]