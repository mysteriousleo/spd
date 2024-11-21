from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.cache import cache_control
import os
import joblib

model1 = joblib.load(os.path.dirname(__file__) + "\\myModel2SVC.pkl")
model2 = joblib.load(os.path.dirname(__file__) + "\\model1.pkl")

# Create your views he
def index(request):
    return render(request, 'index.html')


def checkSpam(request):
    if request.method == 'POST':
      finalAns = None
      algo = request.POST.get("algo")
      rawdata = request.POST.get("rawdata")
      
      if(algo == "Algo-1"):
         finalAns = model1.predict([rawdata])[0]
         param = {"answer" : finalAns}
      elif(algo == "Algo-2"):
         finalAns = model2.predict([rawdata])[0]
         param = {"answer" : finalAns} 
        
      return render(request, 'output.html',param)
    
    else:
       return render(request, 'index.html')