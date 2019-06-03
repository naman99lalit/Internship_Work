from flask import Flask,render_template, redirect, url_for, request, make_response,flash
import datetime,json
import os

app = Flask(__name__)
app.secret_key = 'some_secret'

with open('data.json','r') as outfile:
    dataset = json.load(outfile)

id = 0
dict ={} # Initialising the dictionary to null when server restarts
with open('database.json','w') as f:
    json.dump(dict,f)
    f.close()

@app.route("/") #Login page
def details():
    with open('database.json','r') as f:
        dict = json.load(f)
    return render_template('login.html')


@app.route("/data", methods = ['POST','GET']) #Database Route
def data():
    with open('database.json','r') as f: #Opening the file and passing data
        dict = json.load(f)
        f.close()
    return render_template("data1.html",dict=dict)


@app.route("/index",methods= ['POST','GET']) #Training Page
def index():
    error = None
    if request.method == 'POST':
        id = request.form['Email']
        names = request.form['Name']
        with open('data.json','r') as outfile:
            dataset = json.load(outfile)
        if id in dataset['email']['logins'].values():#checking if the person is in database or not
            if id in dict.keys():#If the person has already logged in first
                with open('database.json','w') as outfile:
                    now = datetime.datetime.now()
                    time1 = now.strftime("%Y-%m-%d  %H:%M:%S")
                    dict[id][2] = time1
                    json.dump(dict,outfile)
                    test = dataset['trainings']
                return render_template("index.html",id=id,names=names,test=test,dict=dict)
            else:
                dict[id] = []#creating a new record of the person
                dict[id].append('Logged In')
                str = ''
                if id in dataset['email']['Security']:#checking to which category does the person belong to
                    str += 'Security'
                if id in dataset['email']['Devops']:
                    if str=='':
                        str += 'Devops'
                    else:
                        str += '& Devops'
                dict[id].append(str)
                now = datetime.datetime.now()
                time1 = now.strftime("%Y-%m-%d  %H:%M:%S")
                dict[id].append(time1) #adding time
                with open('database.json','w') as outfile:
                    json.dump(dict,outfile)
                test = dataset['trainings'] #Passing the data of different types of trainings
                return render_template("index.html",id=id,names=names,test=test,dict=dict)
        else:
            flash('Invalid Credentials! Please check your details.')
    resp=make_response(render_template("login.html",error=error))
    return resp

@app.route("/error/<id>",methods = ['POST' , 'GET']) #Last Page for Anti-Phishing
def error(id):
    if request.method=='POST':
        if request.form['submit']=="http://marketmeddium.com/certification":
            dict[id][4]='Fail'
            now = datetime.datetime.now()
            time1 = now.strftime("%Y-%m-%d  %H:%M:%S")
            dict[id][2]=time1  # Updating the time
            with open('database.json','w') as outfile:
                json.dump(dict,outfile)
            return render_template("error.html")

@app.route("/main/<id>/<names>", methods=['POST','GET']) #Anti-Phishing training page
def main(id,names):
    if request.method=='POST':
        if request.form['Presentation']=="Anti-Phishing":  #Checking whether the button is clicked or not
            now = datetime.datetime.now()
            time1 = now.strftime("%Y-%m-%d  %H:%M:%S")
            dict[id][2]=time1
            dict[id].append('Pass')
            dict[id].append('Pass')
            with open('database.json','w') as outfile:
                json.dump(dict,outfile)
            return render_template("main.html",id=id,names=names)

if __name__=='__main__':
	app.run(debug = True)
