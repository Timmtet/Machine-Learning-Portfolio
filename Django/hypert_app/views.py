from django.http import HttpResponse
from django.shortcuts import render
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

#import the model
model = pickle.load(open('hypert_app/log.pkl', 'rb'))

def predictor(request):
    return render(request, 'main_log.html')

def formInfo(request):
    age = int(request.GET.get('age'))
    sex = int(request.GET.get('sex'))
    cp = int(request.GET.get('cp'))
    trestbps = int(request.GET.get('trestbps'))
    chol = int(request.GET.get('chol'))
    fbs = int(request.GET.get('fbs'))
    restecg = int(request.GET.get('restecg'))
    thalach = int(request.GET.get('thalach'))
    exang = int(request.GET.get('exang'))
    oldpeak = float(request.GET.get('oldpeak'))
    slope = int(request.GET.get('slope'))
    ca = int(request.GET.get('ca'))
    thal = int(request.GET.get('thal'))

    # collect the input data
    features = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    
    #define the column names
    column_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

    #make a dataframe from the input data
    prediction_data = pd.DataFrame([features], columns=column_names)
    
    # Make prediction
    y_pred = model.predict(prediction_data)

    print('The prediction is:', y_pred)
    print(features)

    # Return the result
    if y_pred[0] == 0:
        result = 'not hypertensive' 
    else:
        result = 'hypertensive'
    

    return render(request, 'result_log.html', {'result': result})