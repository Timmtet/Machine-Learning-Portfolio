from django.http import HttpResponse
from django.shortcuts import render

import pickle
from sklearn.preprocessing import LabelEncoder
model = pickle.load(open('a_urinaryApp/decision_tree_model2.pkl', 'rb'))

label_encoder = LabelEncoder()

def predictor(request):
    return render(request, 'main.html')

def formInfo(request):
    Age = request.GET.get('age')
    Gender = request.GET.get('gender')
    Colour = request.GET.get('colour')
    Transparency = request.GET.get('transparency')
    Glucose = request.GET.get('glucose')
    Protein = request.GET.get('protein')
    pH = request.GET.get('ph')
    SpecificGravity = request.GET.get('specific_gravity')
    EpithelialCells = request.GET.get('epithelial_cells')
    MucousThreads = request.GET.get('mucous_threads')
    AmorphousUrates = request.GET.get('amorphous_urates')
    Bacteria = request.GET.get('bacteria')

    gender_encoded = label_encoder.fit_transform([Gender])[0]
    colour_encoded = label_encoder.fit_transform([Colour])[0]
    transparency_encoded = label_encoder.fit_transform([Transparency])[0]
    glucose_encoded = label_encoder.fit_transform([Glucose])[0]
    protein_encoded = label_encoder.fit_transform([Protein])[0]
    epithelial_cells_encoded = label_encoder.fit_transform([EpithelialCells])[0]
    mucous_threads_encoded = label_encoder.fit_transform([MucousThreads])[0]
    amorphous_urates_encoded = label_encoder.fit_transform([AmorphousUrates])[0]
    bacteria_encoded = label_encoder.fit_transform([Bacteria])[0]
    y_pred = model.predict([[Age, gender_encoded, colour_encoded, transparency_encoded, glucose_encoded, protein_encoded, pH, SpecificGravity, epithelial_cells_encoded, mucous_threads_encoded, amorphous_urates_encoded, bacteria_encoded]])
    print(y_pred)
    if y_pred[0] == 0:
        y_pred = 'Negative'
    else:
        y_pred = 'Positive'
    return render(request, 'result.html',  {'result': y_pred})