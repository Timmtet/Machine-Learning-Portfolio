from django.http import HttpResponse
from django.shortcuts import render
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

#import the model
model = pickle.load(open('milk_app/knn.pkl', 'rb'))

def predictor(request):
    return render(request, 'main_knn.html')

def formInfo(request):
    pH = float(request.GET.get('pH'))
    temprature = request.GET.get('Temprature')
    taste = request.GET.get('Taste')
    odor = request.GET.get('Odor')
    fat = request.GET.get('Fat')
    turbidity = request.GET.get('Turbidity')
    colour = request.GET.get('Colour')

    # collect the input data
    features = [pH,temprature,taste,  odor, fat, turbidity, colour]
    
    #define the column names
    column_names = ['pH', 'Temprature', 'Taste', 'Odor', 'Fat ', 'Turbidity', 'Colour']

    #make a dataframe from the input data
    prediction_data = pd.DataFrame([features], columns=column_names)
    
    # Make prediction
    y_pred = model.predict(prediction_data)

    print('The prediction is:', y_pred)
    
    # Return the result
    if y_pred[0] == 0:
        result = 'High' 
    elif y_pred[0] == 1:
        result = 'Low'
    else:
        result = 'Medium'

    return render(request, 'result_knn.html', {'result': result})