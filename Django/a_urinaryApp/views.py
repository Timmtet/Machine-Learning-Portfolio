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

    # encode the input data
    Gender = {'FEMALE': 0, 'MALE': 1}[Gender]
    Colour = {'AMBER': 0, 'BROWN': 1, 'DARK YELLOW': 2, 'LIGHT RED': 3, 'LIGHT YELLOW': 4, 'RED': 5, 'REDDISH': 6, 'REDDISH YELLOW': 7, 'STRAW': 8, 'YELLOW': 9}[Colour]
    Transparency = {'CLEAR': 0, 'CLOUDY': 1, 'HAZY': 2, 'SLIGHTLY HAZY': 3, 'TURBID': 4}[Transparency]
    Glucose = {'1+': 0, '2+': 1, '3+': 2, '4+': 3, 'NEGATIVE': 4, 'TRACE': 5}[Glucose]
    Protein = {'1+': 0, '2+': 1, '3+': 2, 'NEGATIVE': 3, 'TRACE': 4}[Protein]
    EpithelialCells = {'FEW': 0, 'LOADED': 1, 'MODERATE': 2, 'NONE SEEN': 3, 'OCCASIONAL': 4, 'PLENTY': 5, 'RARE': 6}[EpithelialCells]
    MucousThreads = {'FEW': 0, 'LOADED': 1, 'MODERATE': 2, 'NONE SEEN': 3, 'OCCASIONAL': 4, 'PLENTY': 5, 'RARE': 6}[MucousThreads]
    AmorphousUrates = {'FEW': 0, 'LOADED': 1, 'MODERATE': 2, 'NONE SEEN': 3, 'OCCASIONAL': 4, 'PLENTY': 5, 'RARE': 6}[AmorphousUrates]
    Bacteria = {'FEW': 0, 'LOADED': 1, 'MODERATE': 2, 'NONE SEEN': 3, 'OCCASIONAL': 4, 'PLENTY': 5, 'RARE': 6}[Bacteria]

    y_pred = model.predict([[Age, Gender, Colour, Transparency, Glucose, Protein, pH, SpecificGravity, EpithelialCells, MucousThreads, AmorphousUrates, Bacteria]])
    print(y_pred)
    if y_pred[0] == 0:
        y_pred = 'Negative'
    else:
        y_pred = 'Positive'
    return render(request, 'result.html',  {'result': y_pred})