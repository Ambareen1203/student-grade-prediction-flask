from flask import Flask, request
from flask.templating import render_template
from app import app
from user.models import User




@app.route("/user/signup", methods=['POST'])
def signup():
    return User().signup()

@app.route('/user/signout')
def signout():
    return User().signout()

@app.route('/user/login', methods=['POST'])
def login():
    return User().login()

@app.route('/user/dashboard/module')
def module():
    return render_template('module.html')

@app.route('/user/dashboard/studentGrades', methods=['GET', 'POST'])

def studentGrades():
    if request.method == 'POST':
        return User().studentGrades()
        
    else:
        return render_template('studentGrades.html')

@app.route('/user/dashboard/predict1')
def predict1():
    return render_template('predict1.html')

@app.route('/user/dashboard/predict2')
def predict2():
    return render_template('predict2.html')

@app.route('/user/dashboard/predict3')
def predict3():
    return render_template('predict3.html')

@app.route('/user/dashboard/predict4')
def predict4():
    return render_template('predict4.html')

@app.route('/user/dashboard/predict5')
def predict5():
    return render_template('predict5.html')

@app.route('/user/dashboard/predict6')
def predict6():
    return render_template('predict6.html')

    
        


    




    







    







