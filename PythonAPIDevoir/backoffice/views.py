from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    return HttpResponse("Bonjour monde!")

def predict_medv(unscaled_data):
    from sklearn.externals import joblib
    colonnes        = ["1", "2","3"]
    path_to_model   = "./ipynb/model_simple.sav"
    path_for_scaler = "./ipynb/scaler.sav"
    unscaled_data   = [unscaled_data[colonne] for colonne in colonnes]
    model           = joblib.load(path_to_model)
    scaler          = joblib.load(path_for_scaler)
    donnees_scalees = scaler.transform([unscaled_data])
    medv            = model.predict(donnees_scalees)
    return medv

@csrf_exempt
def predict(request):
    """
    Renvoie une house avec la MEDV completee
    (Attend une MEDV innexistante == null)
    """
    if request.method == 'GET':
       # return     JsonResponse(serializer.errors, status=400)
        return predict_medv(JSONParser().parse(request))
    elif request.method == 'POST':
        data        = JSONParser().parse(request)
        #data["MEDV"]        = predict_medv(data)
        #return     JsonResponse(serializer.errors, status=400)
        return predict_medv(data)

