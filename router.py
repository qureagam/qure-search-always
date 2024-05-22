from flask import Flask,render_template,request
from wiki import *
from google_links import *
from news import *
from  mail_sender import *

app = Flask(__name__)

@app.route('/')
def searching():
    return render_template('index.html')

@app.route('/',methods=["GET","POST"])
def Search_Return():
    if request.method =="POST":
        globaling = request.form.get('QURE')
        raw_question = {
           "nude" : request.form.get('QURE'),
           "wik":wiki(globaling),
           "goal":link(globaling)
            }
        try:
         return render_template('result.html',
                               data1 = raw_question["nude"],
                               data2 = raw_question["wik"],
                               data3 = raw_question["goal"]
                               )
        except Exception as s:
            return render_template('error.html',man ="Try later")
    else:
         return render_template('index.html')


@app.route("/more")
def service():
    try:
       multi_data = {
           "nedata" : news_all_today()
       }
       return render_template('policy.html',news = multi_data["nedata"],dealer="India's Todays News")
    except Exception as fr:
        return render_template('policy.html',dealer="Network Problem")

@app.route("/contact",methods = ["GET","POST"])
def contact():
    return render_template("contact.html")

@app.route("/contact",methods = ["GET","POST"])
def send():
    try:
     if request.method =="Post":
       body = request.form.get("text")
       name = request.form.get("mal")
       passw = request.form.get("passw")
       sending_mail(name,passw,body)
       return render_template("contact.html")
     else:
        render_template("error.html")
    except Exception as fro:
       render_template("error.html",man = "Allow 2-step verification")


if __name__ =='__main__':
    app.run(debug = False,host="0.0.0.0")



