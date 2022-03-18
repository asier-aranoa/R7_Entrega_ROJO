from re import A
from flask import Flask, request, render_template, url_for, session
from werkzeug.utils import secure_filename
import pickle
import numpy as np
import pandas as pd
import funciones
from funciones1 import fun
import xlrd

app = Flask(__name__)

app.secret_key='secret_key'

with open('model2.pkl','rb') as handle:
    model = pickle.load(handle)

with open('model_industria.pkl','rb') as handle:
    model2 = pickle.load(handle)

############################
@app.route("/", methods = ['GET','POST'])  
def home():
    if request.method == 'GET':
        return render_template('inicio.html')
    else:
        return render_template('inicio.html')

@app.route("/general", methods = ['GET','POST'])  
def general():
    if request.method == 'GET':
        return render_template('inicio_general.html')
    else:
        return render_template('inicio_general.html')

@app.route("/generalcsv", methods = ['GET','POST'])  
def generalcsv():
    if request.method == 'GET':
        return render_template('upload_general.html')
    else:
        f = request.files['file'] # es lo mismo que hacer   f = request.files.get('file')
        df = pd.read_csv(f)
        x=fun(df)
        for a in x:
            if a=='act_cor':
                act_cor = df[a][0]
            if a=='act_no_cor':
                act_no_cor = df[a][0]
            if a=='patri_neto':
                patri_neto = df[a][0]
            if a=='pasivo_cor':
                pasivo_cor = df[a][0]
            if a=='pasivo_no_cor':
                pasivo_no_cor = df[a][0]
            if a=='roa':
                roa = df[a][0]
            if a=='roe':
                roe = df[a][0]
            if a=='act_cor_1':
                act_cor_1 = df[a][0]
            if a=='act_no_cor_1':
                act_no_cor_1 = df[a][0]
            if a=='patri_neto_1':
                patri_neto_1 = df[a][0]
            if a=='pasivo_cor_1':
                pasivo_cor_1 = df[a][0]
            if a=='pasivo_no_cor_1':
                pasivo_no_cor_1 = df[a][0]
            if a=='roa_1':
                roa_1 = df[a][0]
            if a=='roe_1':
                roe_1 = df[a][0]
            if a=='act_cor_2':
                act_cor_2 = df[a][0]
            if a=='act_no_cor_2':
                act_no_cor_2 = df[a][0]
            if a=='patri_neto_2':
                patri_neto_2 = df[a][0]
            if a=='pasivo_cor_2':
                pasivo_cor_2 = df[a][0]
            if a=='pasivo_no_cor_2':
                pasivo_no_cor_2 = df[a][0]
            if a=='roa_2':
                roa_2 = df[a][0]
            if a=='roe_2':
                roe_2 = df[a][0]
            if a=='act_cor_3':
                act_cor_3 = df[a][0]
            if a=='act_no_cor_3':
                act_no_cor_3 = df[a][0]
            if a=='patri_neto_3':
                patri_neto_3 = df[a][0]
            if a=='pasivo_cor_3':
                pasivo_cor_3 = df[a][0]
            if a=='pasivo_no_cor_3':
                pasivo_no_cor_3 = df[a][0]
            if a=='roa_3':
                roa_3 = df[a][0]
            if a=='roe_3':
                roe_3 = df[a][0]
        features = funciones.resultado(act_cor,act_no_cor,patri_neto,pasivo_cor,pasivo_no_cor,roa,roe,act_cor_1,act_no_cor_1,patri_neto_1,pasivo_cor_1,pasivo_no_cor_1,roa_1,roe_1,act_cor_2,act_no_cor_2,patri_neto_2,pasivo_cor_2,pasivo_no_cor_2,roa_2,roe_2,act_cor_3,act_no_cor_3,patri_neto_3,pasivo_cor_3,pasivo_no_cor_3,roa_3,roe_3)
        final_features = [np.array(features)]    
        prediction = model.predict(final_features)  
        prediction = prediction[0]    
        return render_template('resultado.html', prediction = prediction,act_cor=act_cor,act_no_cor=act_no_cor,patri_neto=patri_neto,
        pasivo_cor=pasivo_cor,pasivo_no_cor=pasivo_no_cor,roa=roa,roe=roe)

@app.route("/generalmano", methods = ['GET','POST'])  
def generalmano():
    if request.method == 'GET':
        return render_template('login_general.html')
    else:
        act_cor = float(request.form.get('act_cor'))
        act_no_cor = float(request.form.get('act_no_cor'))
        patri_neto = float(request.form.get('patri_neto'))
        pasivo_cor = float(request.form.get('pasivo_cor'))
        pasivo_no_cor = float(request.form.get('pasivo_no_cor'))
        roa= float(request.form.get('ROA'))
        roe= float(request.form.get('ROE'))
        act_cor_1 = float(request.form.get('act_cor_1'))
        act_no_cor_1 = float(request.form.get('act_no_cor_1'))
        patri_neto_1 = float(request.form.get('patri_neto_1'))
        pasivo_cor_1 = float(request.form.get('pasivo_cor_1'))
        pasivo_no_cor_1 = float(request.form.get('pasivo_no_cor_1'))
        roa_1= float(request.form.get('ROA_1'))
        roe_1= float(request.form.get('ROE_1'))
        act_cor_2 = float(request.form.get('act_cor_2'))
        act_no_cor_2 = float(request.form.get('act_no_cor_2'))
        patri_neto_2 = float(request.form.get('patri_neto_2'))
        pasivo_cor_2 = float(request.form.get('pasivo_cor_2'))
        pasivo_no_cor_2 = float(request.form.get('pasivo_no_cor_2'))
        roa_2= float(request.form.get('ROA_2'))
        roe_2= float(request.form.get('ROE_2'))
        act_cor_3 = float(request.form.get('act_cor_3'))
        act_no_cor_3 = float(request.form.get('act_no_cor_3'))
        patri_neto_3 = float(request.form.get('patri_neto_3'))
        pasivo_cor_3 = float(request.form.get('pasivo_cor_3'))
        pasivo_no_cor_3 = float(request.form.get('pasivo_no_cor_3'))
        roa_3= float(request.form.get('ROA_3'))
        roe_3= float(request.form.get('ROE_3'))
        features = funciones.resultado(act_cor,act_no_cor,patri_neto,pasivo_cor,pasivo_no_cor,roa,roe,act_cor_1,act_no_cor_1,patri_neto_1,pasivo_cor_1,pasivo_no_cor_1,roa_1,roe_1,act_cor_2,act_no_cor_2,patri_neto_2,pasivo_cor_2,pasivo_no_cor_2,roa_2,roe_2,act_cor_3,act_no_cor_3,patri_neto_3,pasivo_cor_3,pasivo_no_cor_3,roa_3,roe_3)
        final_features = [np.array(features)]  
        prediction = model.predict(final_features)  
        prediction = prediction[0]    
        return render_template('resultado.html', prediction = prediction,act_cor=act_cor,act_no_cor=act_no_cor,patri_neto=patri_neto,
        pasivo_cor=pasivo_cor,pasivo_no_cor=pasivo_no_cor,roa=roa,roe=roe)
    

@app.route("/transporte", methods = ['GET','POST'])  
def transporte():
    if request.method == 'GET':
        return render_template('inicio_transporte.html')
    else:
        return render_template('inicio_transporte.html')

@app.route("/transportecsv", methods = ['GET','POST'])  
def transportecsv():
    if request.method == 'GET':
        return render_template('upload_transporte.html')
    else:
        f = request.files['file'] # es lo mismo que hacer   f = request.files.get('file')
        df = pd.read_csv(f)
        x=fun(df)
        for a in x:
            if a=='act_cor':
                act_cor = df[a][0]
            if a=='act_no_cor':
                act_no_cor = df[a][0]
            if a=='patri_neto':
                patri_neto = df[a][0]
            if a=='pasivo_cor':
                pasivo_cor = df[a][0]
            if a=='pasivo_no_cor':
                pasivo_no_cor = df[a][0]
            if a=='roa':
                roa = df[a][0]
            if a=='roe':
                roe = df[a][0]
            if a=='act_cor_1':
                act_cor_1 = df[a][0]
            if a=='act_no_cor_1':
                act_no_cor_1 = df[a][0]
            if a=='patri_neto_1':
                patri_neto_1 = df[a][0]
            if a=='pasivo_cor_1':
                pasivo_cor_1 = df[a][0]
            if a=='pasivo_no_cor_1':
                pasivo_no_cor_1 = df[a][0]
            if a=='roa_1':
                roa_1 = df[a][0]
            if a=='roe_1':
                roe_1 = df[a][0]
            if a=='act_cor_2':
                act_cor_2 = df[a][0]
            if a=='act_no_cor_2':
                act_no_cor_2 = df[a][0]
            if a=='patri_neto_2':
                patri_neto_2 = df[a][0]
            if a=='pasivo_cor_2':
                pasivo_cor_2 = df[a][0]
            if a=='pasivo_no_cor_2':
                pasivo_no_cor_2 = df[a][0]
            if a=='roa_2':
                roa_2 = df[a][0]
            if a=='roe_2':
                roe_2 = df[a][0]
            if a=='act_cor_3':
                act_cor_3 = df[a][0]
            if a=='act_no_cor_3':
                act_no_cor_3 = df[a][0]
            if a=='patri_neto_3':
                patri_neto_3 = df[a][0]
            if a=='pasivo_cor_3':
                pasivo_cor_3 = df[a][0]
            if a=='pasivo_no_cor_3':
                pasivo_no_cor_3 = df[a][0]
            if a=='roa_3':
                roa_3 = df[a][0]
            if a=='roe_3':
                roe_3 = df[a][0]
        features = funciones.resultado(act_cor,act_no_cor,patri_neto,pasivo_cor,pasivo_no_cor,roa,roe,act_cor_1,act_no_cor_1,patri_neto_1,pasivo_cor_1,pasivo_no_cor_1,roa_1,roe_1,act_cor_2,act_no_cor_2,patri_neto_2,pasivo_cor_2,pasivo_no_cor_2,roa_2,roe_2,act_cor_3,act_no_cor_3,patri_neto_3,pasivo_cor_3,pasivo_no_cor_3,roa_3,roe_3)
        final_features = [np.array(features)]      
        prediction = model2.predict(final_features)  
        prediction = prediction[0]    
        return render_template('resultado.html', prediction = prediction,act_cor=act_cor,act_no_cor=act_no_cor,patri_neto=patri_neto,
        pasivo_cor=pasivo_cor,pasivo_no_cor=pasivo_no_cor,roa=roa,roe=roe)

@app.route("/transportemano", methods = ['GET','POST'])  
def transportemano():
    if request.method == 'GET':
        return render_template('login_transporte.html')
    else:
        act_cor = float(request.form.get('act_cor'))
        act_no_cor = float(request.form.get('act_no_cor'))
        patri_neto = float(request.form.get('patri_neto'))
        pasivo_cor = float(request.form.get('pasivo_cor'))
        pasivo_no_cor = float(request.form.get('pasivo_no_cor'))
        roa= float(request.form.get('ROA'))
        roe= float(request.form.get('ROE'))
        act_cor_1 = float(request.form.get('act_cor_1'))
        act_no_cor_1 = float(request.form.get('act_no_cor_1'))
        patri_neto_1 = float(request.form.get('patri_neto_1'))
        pasivo_cor_1 = float(request.form.get('pasivo_cor_1'))
        pasivo_no_cor_1 = float(request.form.get('pasivo_no_cor_1'))
        roa_1= float(request.form.get('ROA_1'))
        roe_1= float(request.form.get('ROE_1'))
        act_cor_2 = float(request.form.get('act_cor_2'))
        act_no_cor_2 = float(request.form.get('act_no_cor_2'))
        patri_neto_2 = float(request.form.get('patri_neto_2'))
        pasivo_cor_2 = float(request.form.get('pasivo_cor_2'))
        pasivo_no_cor_2 = float(request.form.get('pasivo_no_cor_2'))
        roa_2= float(request.form.get('ROA_2'))
        roe_2= float(request.form.get('ROE_2'))
        act_cor_3 = float(request.form.get('act_cor_3'))
        act_no_cor_3 = float(request.form.get('act_no_cor_3'))
        patri_neto_3 = float(request.form.get('patri_neto_3'))
        pasivo_cor_3 = float(request.form.get('pasivo_cor_3'))
        pasivo_no_cor_3 = float(request.form.get('pasivo_no_cor_3'))
        roa_3= float(request.form.get('ROA_3'))
        roe_3= float(request.form.get('ROE_3'))
        features = funciones.resultado(act_cor,act_no_cor,patri_neto,pasivo_cor,pasivo_no_cor,roa,roe,act_cor_1,act_no_cor_1,patri_neto_1,pasivo_cor_1,pasivo_no_cor_1,roa_1,roe_1,act_cor_2,act_no_cor_2,patri_neto_2,pasivo_cor_2,pasivo_no_cor_2,roa_2,roe_2,act_cor_3,act_no_cor_3,patri_neto_3,pasivo_cor_3,pasivo_no_cor_3,roa_3,roe_3)
        final_features = [np.array(features)]      
        prediction = model2.predict(final_features)  
        prediction = prediction[0]    
        return render_template('resultado.html', prediction = prediction,act_cor=act_cor,act_no_cor=act_no_cor,patri_neto=patri_neto,
        pasivo_cor=pasivo_cor,pasivo_no_cor=pasivo_no_cor,roa=roa,roe=roe)






if __name__ == "__main__":
    app.run(debug=True)

