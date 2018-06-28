import os
import pandas as pd 
import pickle
import numpy as np
from flask import Flask, jsonify, request, Markup, render_template
from statsmodels.tsa.arima_model import ARIMA

app = Flask(__name__)
app.debug = True


def util():
    filename = 'model.pk'
    print("Loading Model")
    loaded_model = None
    with open(r'C:\users\abhij\Desktop\Amdocs\\' + filename,'rb') as file:
         loaded_model = pickle.load(file)

    print("Doing predictions: ")
    predictions = loaded_model.predict(start=30,end=500)
   
    values = []
    for i in range(439):
       values.append(predictions[i])
    return values  
@app.route('/predict')
def apicall():           
    return render_template('index.html',values=util())    

@app.route('/')
def home():
     filename = 'actual'
     with open(r'C:\users\abhij\Desktop\Amdocs\\' + filename,'rb') as file:
         actualdata = pickle.load(file)
     print("Showing Actual data:")

     values = []
     for i in range(100):
         values.append(actualdata[i])     
     

     return render_template('previous.html',values= values)

@app.route('/loading')
def load():
    return render_template('loading.html')

@app.route('/stabilize')
def do():
    return render_template('stabilize.html',values=util())

if __name__ == "__main__":
    app.run()    
    
     