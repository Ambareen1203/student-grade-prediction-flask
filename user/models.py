import user
from flask import Flask, jsonify, request, session, redirect, url_for
from flask.templating import render_template
from passlib.hash import pbkdf2_sha256
import uuid
from app import db
from bson import ObjectId
from pycaret.regression import *



class User:

    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200
    
    def signup(self):
        print(request.form)

        # Create the user object
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password'),
            "gender": request.form.get('gender'),
            "region": request.form.get('region'),
            "highest_education": request.form.get('highest_education'),
            "imd_band": request.form.get('imd_band'),
            "age_band": request.form.get('age_band'),
            "disability": request.form.get('disability'),
            "modules": request.form.get('modules'),
            "tma1": request.form.get('tma1'),
            "tma2": request.form.get('tma2'),
            "tma3": request.form.get('tma3'),
            "tma4": request.form.get('tma4'),
            "tma5": request.form.get('tma5'),
            "tma6": request.form.get('tma6'),
            "weighted_grade": request.form.get('weighted_grade'),
            "total_click": request.form.get('total_click')
            

            
        }

        # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        # Check for existing email address 
        if db.users.find_one({"email": user['email'] }):
            return jsonify({ "error": "Email address already in use" }), 400

        if db.users.insert_one(user):
            return self.start_session(user)
    

        return jsonify({ "error": "Signup failed" }), 400

    def signout(self):
        session.clear()
        return redirect('/')

    def login(self):
        
        
        user = db.users.find_one({
            "email": request.form.get('email')
        })

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']): 
            return self.start_session(user)
            

        return jsonify({ "error": "Invalid email address or password provided"}), 401

    def studentGrades(self):

        db.users.update_one(
            {"_id": "08b99d3b7013476494e178af85020406" },
             {"$set":
            
            {
            "weighted_grade":request.form.get('weighted_grade'),
            "total_click": request.form.get('total_click')
             }})
             
            
            
             

        return jsonify({ "success": "Grade successfully uploaded"}), 201

    


   
   

    

    

    


    


    
    
             
    
    
    
            
            

         

      
    




    