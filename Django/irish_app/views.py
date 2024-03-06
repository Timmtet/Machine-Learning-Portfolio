from django.http import HttpResponse
from django.shortcuts import render

import pickle
from sklearn.preprocessing import LabelEncoder
model = pickle.load(open('irish_app/naive_bayes.pkl', 'rb'))

def predictor(request):
    return render(request, 'main_nbm.html')

def formInfo(request):
    sepal_length = float(request.GET.get('sepal_length'))
    sepal_width = float(request.GET.get('sepal_width'))
    petal_length = float(request.GET.get('petal_length'))
    petal_width = float(request.GET.get('petal_width'))
    y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    print( 'The prediction is:', y_pred)
    if y_pred[0] == 0:
        y_pred = 'Setosa'
    elif y_pred[0] == 1:
        y_pred = 'Versicolor'
    else:
        y_pred = 'Virginica'
    return render(request, 'result_nbm.html',  {'result': y_pred})