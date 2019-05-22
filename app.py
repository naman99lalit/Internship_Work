from flask import Flask,render_template, redirect, url_for, request, make_response,flash
import datetime
app = Flask(__name__)
app.secret_key = 'some_secret'

now = datetime.datetime.now()
global value,time1
value = 0
time1 = 0
dict = {}
arr=[]
logins = {
    'naman':'naman.lalit@marketmedium.com',
    'Abhishek Verma': 'abhishek.verma@marketmedium.com',
    'Apoorv Mangal Pandey': 'apoorv.pandey@marketmedium.com',
    'Hariprasad Kulkarni': 'hariprasad.kulkarni@marketmedium.com',
    'Bharath Sridhar': 'bharath.sridhar@marketmedium.com',
    'Swati Soni': 'swati.soni@marketmedium.com',
    'Mariet Nilappana': 'Mariet.Nilappana@marketmedium.com',
    'Chaitanya Chinni ': 'chaitanya.chinni@marketmedium.com',
    'Preetham Angadi': 'preetham.angadi@marketmedium.com',
    'Laxman Kadam': 'laxman.kadam@marketmedium.com',
    'Sudeep Reddy': 'sudeep.reddy@marketmedium.com',
}
@app.route("/")
def details():
    return render_template('login.html')

@app.route("/data", methods = ['POST','GET'])
def data():
    return render_template("data1.html",dict=dict)

@app.route("/index",methods= ['POST','GET'])
def index():
    error = None
    if request.method=='POST':
        value = request.form['Email']
        names=request.form['Name']
        if value in logins.values():
            dict[value]=['0']
            dict[value].append('Logged In')
            return render_template("index.html",value=value,names=names)
        else:
            flash('Invalid Credentials! Please check your details.')
    resp=make_response(render_template("login.html",error=error))
    return resp

@app.route("/error/<value>",methods = ['POST' , 'GET'])
def error(value):
    if request.method=='POST':
        if request.form['submit']=="http://marketmeddium.com/certification":
            dict[value].append('Fail')
            print(value)
            print(dict)
            return render_template("error.html")

@app.route("/main/<value>/<names>", methods=['POST','GET'])
def main(value,names):
    if request.method=='POST':
        if request.form['Presentation']==" Training ":
            dict[value].append('Pass')
            time1 = now.strftime("%Y-%m-%d")
            dict[value].append(time1)
            print(dict)
            return render_template("main.html",value=value,names=names)

if __name__=='__main__':
	app.run(debug = True)
