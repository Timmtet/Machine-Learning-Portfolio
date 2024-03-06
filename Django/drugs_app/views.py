from django.http import HttpResponse
from django.shortcuts import render

import pickle
from sklearn.preprocessing import LabelEncoder
model = pickle.load(open('drugs_app/svm.pkl', 'rb'))

def predictor(request):
    return render(request, 'main_svm.html')

def formInfo(request):
    age = int(request.GET.get('age'))
    gender = request.GET.get('gender')
    blood_pressure = request.GET.get('blood_pressure')
    cholesterol = request.GET.get('cholesterol')
    na_to_k = float(request.GET.get('na_to_k'))

    gender = 0 if gender == 'F' else 1
    blood_pressure = {'HIGH': 0, 'LOW': 1, 'NORMAL': 2}[blood_pressure]
    cholesterol = {'HIGH': 0, 'NORMAL': 1}[cholesterol]

    y_pred = model.predict([[age, gender, blood_pressure, cholesterol, na_to_k]])
    print( 'The prediction is:', y_pred)
    if y_pred[0] == 0:
        y_pred = 'DrugA'
    elif y_pred[0] == 1:
        y_pred = 'DrugB'
    elif y_pred[0] == 2:
        y_pred = 'DrugC'
    elif y_pred[0] == 3:
        y_pred = 'DrugX'
    else:
        y_pred = 'DrugY'
  
    return render(request, 'result_svm.html',  {'result': y_pred})