
from flask import Flask, render_template, request, redirect
import pickle
import sklearn
import numpy as np                        
import os


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':

        with open('models/air_model1.sav', 'rb') as r:
            model = pickle.load(r)

        ph = float(request.form['ph'])
        Hardness = float(request.form['Hardness'])
        Solids = float(request.form['Solids'])
        Chloramines = float(request.form['Chloramines'])
        Sulfate = float(request.form['Sulfate'])
        Conductifity = float(request.form['Conductifity'])
        Organic_carbon = float(request.form['Organic Carbon'])
        Trihalomethanes = float(request.form['Trihalomethanes'])
        Turbidity = float(request.form['Turbidity'])

        datas = np.array((ph,Hardness,Solids,Chloramines,Sulfate,Conductifity,Organic_carbon,Trihalomethanes,Turbidity))
        datas = np.reshape(datas, (1, -1))

        ispotability = model.predict(datas)

        return render_template('hasil.html', finalData=ispotability)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)