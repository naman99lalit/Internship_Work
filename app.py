from flask import Flask,render_template, redirect, url_for, request, make_response
app = Flask(__name__)

array = []

@app.route("/")
def details():
    return render_template('login.html')

@app.route("/data", methods = ['POST','GET'])
def data():
    return render_template("data.html",len = len(array), array=array)

@app.route("/error",methods = ['POST' , 'GET'])
def error():
    if request.method=='POST':
        value = request.form['Name']
        print(value)
        if(value not in array):
            array.append(value)
        print(array)
    return render_template("error.html")
if __name__=='__main__':
	app.run(debug = True)
