from django.urls import path
from . import views

urlpatterns = [
    path('svm/', views.predictor, name='predictor'),
    path('result', views.formInfo, name='result'),
    path('svm/result', views.formInfo, name='result'),
]