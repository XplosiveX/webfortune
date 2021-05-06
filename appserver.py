from flask import Flask, render_template, request, session, redirect, url_for, jsonify, abort
import os

app = Flask(__name__)

##tests to make sure files exist.
try:
    cow = open("cowsay.txt")
    fortune = open("fortune.txt")
    cow.close()
    fortune.close()
    # Do something with the file
except:
    try:
        open("cowsay.txt", "x")
    except:
        pass
    try:
        open("fortune.txt", "x")
    except:
        pass
returnvalue = ""
#this is supposed to load an index.html and render
##@app.route('/')
##def hello():
    ##return render_template('index.html', title='Welcome', members=users)


@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/', methods=['GET'])
def fortune():
    os.system("fortune >> fortune.txt")
    with open("fortune.txt", "r") as file:
        returnvalue = file.read()
        valueof = "<pre>" + returnvalue + "</pre>"
        closer = open("fortune.txt","w")
    closer.close()
    returnvalue.close()
    return valueof

@app.route('/cowsay/<string:message>/', methods=['GET'])
def cowsay(message):
    os.system("cowsay " + message + ">> cowsay.txt")
    with open("fortune.txt", "r") as file:
        returnvalue = file.read()
        valueof = "<pre>" + returnvalue + "</pre>"
        closer = open("cowsay.txt","w")
    closer.close()
    returnvalue.close()
    return valueof


@app.route('/cowfortune/', methods=['GET'])
def cowfortune():
    # cowsay stuff
    os.system("cowsay `fortune` >> cowsay.txt")
    with open("cowsay.txt", "r") as file:
        returnvalue = file.read()
        valueof = "<pre>" + returnvalue + "</pre>"
        closer = open("cowsay.txt","w")
    closer.close()
    returnvalue.close()
    return valueof
