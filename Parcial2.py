# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 22:47:50 2021

"""
from flask import Flask,jsonify,request
import pandas as pd

app = Flask(__name__)

df=pd.read_csv('datos.csv')

df = df.convert_dtypes()


@app.route('/Datos')
def Showalldata():
    Datos = df.dropna(1)
    Datos = Datos.to_json(orient='index')
    return jsonify(Datos)



@app.route('/Datos/<string:Pais>')
def FiltroPaises(Pais):
    filtro = df[df['Country Name']==Pais]
    filtro = filtro.dropna(1)
    Datos = filtro.to_json(orient='index')
    return jsonify(Datos)

@app.route('/Datos/<string:Pais>/<string:Years>')
def FiltroYear(Pais,Years):
    filtro = df[df['Country Name']==Pais]
    filtro = filtro.dropna(1)
    Yearlist = Years.split(',')
    filtroyear = filtro[Yearlist]
    Datos = filtroyear.to_json(orient='index')
    return jsonify(Datos)


if __name__== "__main__":
    app.run(debug=True,port=5000)