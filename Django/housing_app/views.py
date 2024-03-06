from django.http import HttpResponse
from django.shortcuts import render
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

#import the model
model = pickle.load(open('housing_app/lin.pkl', 'rb'))

def predictor(request):
    return render(request, 'main_lin.html')

def formInfo(request):
    area = int(request.GET.get('area'))
    bedrooms = int(request.GET.get('bedrooms'))
    bathrooms = int(request.GET.get('bathrooms'))
    stories = int(request.GET.get('stories'))
    mainroad = 1 if request.GET.get('mainroad') == 'yes' else 0
    guestroom = 1 if request.GET.get('guestroom') == 'yes' else 0
    basement = 1 if request.GET.get('basement') == 'yes' else 0
    hotwaterheating = 1 if request.GET.get('hotwaterheating') == 'yes' else 0
    airconditioning = 1 if request.GET.get('airconditioning') == 'yes' else 0
    parking = int(request.GET.get('parking'))
    prefarea = 1 if request.GET.get('prefarea') == 'yes' else 0
    furnishingstatus = request.GET.get('furnishingstatus')


     # encode the furnishingstatus
    furnishingstatus_mapping = {'furnished': 0, 'semi-furnished': 1, 'not-furnished': 2}
    furnishingstatus = furnishingstatus_mapping.get(request.GET.get('furnishingstatus'))

    # collect the input data
    features = [area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating, airconditioning, parking, prefarea, furnishingstatus]
    
    #define the column names
    column_names = ['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea', 'furnishingstatus']

    #make a dataframe from the input data
    prediction_data = pd.DataFrame([features], columns=column_names)
    
    # Make prediction
    y_pred = model.predict(prediction_data)

    print('The prediction is:', y_pred)

    # Return the result
    result = int(y_pred[0])
    

    return render(request, 'result_lin.html', {'result': result})