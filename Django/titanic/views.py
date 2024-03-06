from django.http import HttpResponse
from django.shortcuts import render
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

#import the model
model = pickle.load(open('titanic/rfm.pkl', 'rb'))

def predictor(request):
    return render(request, 'main_rfm.html')

def formInfo(request):
    age = int(request.GET.get('age'))
    gender = request.GET.get('gender')
    pclass = int(request.GET.get('pclass'))
    siblings_spouse = int(request.GET.get('siblings_spouse'))
    parents_children = int(request.GET.get('parents_children'))
    fare = float(request.GET.get('fare'))
    embarkation_port = request.GET.get('embarkation_port')

    # encode the input data
    gender = 0 if gender == 'female' else 1
    embarkation_port = {'Cherbourg': 0, 'Queenstown': 1, 'Southampton': 2}[embarkation_port]

    # collect the input data
    features = [pclass,gender,age,  siblings_spouse, parents_children, fare, embarkation_port]

    #define the column names
    column_names = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']

    #make a dataframe from the input data
    prediction_data = pd.DataFrame([features], columns=column_names)

    # Make prediction
    y_pred = model.predict(prediction_data)

    print('The prediction is:', y_pred)
    
    # Return the result
    if y_pred[0] == 0:
        result = 'Not Survived' 
    else:
        result = 'Survived'

    return render(request, 'result_rfm.html', {'result': result})