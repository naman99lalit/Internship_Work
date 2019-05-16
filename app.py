from flask import Flask,render_template, redirect, url_for, request, make_response,pandas
import requests as rq
app = Flask(__name__)

array = []
@app.route('/', methods = ['POST', 'GET'])
def details():
    name = request.form['FullName']
    array.append(name)
    return render_template('error.html')

@app.route('/data', methods = ['POST'])
def data():
   render_template('data.html') 