from logging import StrFormatStyle
from flask import Flask, render_template, session, redirect, url_for, request
from pycaret.regression import *
import pandas as pd
import numpy as np
from functools import wraps
from flask_pymongo import pymongo


app = Flask(__name__)
app.secret_key= b"&\xe3\xf2\xd7\xb1\xf1\xf7O\x16'\x85H\xe4U\x06I"

# Database

CONNECTION_STRING = "mongodb+srv://Ambareen:winterIScoming21897@cluster0.ecj03.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.user_login

# Models

modelfor6 = load_model('modelClassification6')
modelfor5 = load_model('modelClassification5')
modelfor4 = load_model('modelClassification4')
modelfor3 = load_model('modelClassification3')
modelfor2 = load_model('modelClassification2')
modelfor1 = load_model('modelClassification1')



cols = ['imd_band', 'highest_education', 'weighted_grade', 'total_click']


# Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for("home", next=request.url))

    return wrap


# Routes
from user import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/user/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/predict01',methods=['POST'])
def predict01():

    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = predict_model(modelfor1, data=data_unseen, round = 0)
    prediction = int(prediction.Label[0])
    if prediction == "7":
        res='Fail, your expected marks is between 0 to 40.'
    return render_template('predict1.html',pred='Expected final grade will be {}'.format(prediction))
    


@app.route('/predict02',methods=['POST'])
def predict02():

    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = predict_model(modelfor2, data=data_unseen, round = 0)
    prediction = int(prediction.Label[0])
    return render_template('predict2.html',pred='Expected final grade will be {}'.format(prediction))

@app.route('/predict03',methods=['POST'])
def predict03():

    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = predict_model(modelfor3, data=data_unseen, round = 0)
    prediction = int(prediction.Label[0])
    return render_template('predict3.html',pred='Expected final grade will be {}'.format(prediction))

@app.route('/predict04',methods=['POST'])
def predict04():

    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = predict_model(modelfor4, data=data_unseen, round = 0)
    prediction = int(prediction.Label[0])
    return render_template('predict4.html',pred='Expected final grade will be {}'.format(prediction))

@app.route('/predict05',methods=['POST'])
def predict05():

    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = predict_model(modelfor5, data=data_unseen, round = 0)
    prediction = int(prediction.Label[0])
    return render_template('predict5.html',pred='Expected final grade will be {}'.format(prediction))

@app.route('/predict06',methods=['POST'])
def predict06():

    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = predict_model(modelfor6, data=data_unseen, round = 0)
    prediction = int(prediction.Label[0])
   
    return render_template('predict6.html',pred='Expected final grade will be {}'.format(prediction))








    

 
  
    
    
 
    
    

    


