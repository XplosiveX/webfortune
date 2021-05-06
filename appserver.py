from flask import Flask, render_template, request, session, redirect, url_for, jsonify, abort
import os
import subprocess
import uuid 

app = Flask(__name__)
app.secret_key = str(uuid.uuid4().hex)

@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortunenormal():
    fortune = subprocess.check_output(["fortune"]).decode()
    prereturn = "<pre>" + fortune + "</pre>"
    return prereturn

@app.route('/cowsay/<message>/')
def cowsaynormal(message):
    arg_list = ["cowsay"] + message.split()
    cow= subprocess.check_output(arg_list).decode()
    prereturn = "<pre>" + cow + "</pre>"
    return prereturn

@app.route('/cowfortune/')
def cowsayfortune():
    outcollect = subprocess.check_output(["fortune"]).decode()
    argtodecode = ["cowsay"] + outcollect.split()
    fortunecow = subprocess.check_output(argtodecode).decode()
    prereturn = "<pre>" + fortunecow + "</pre>"
    return prereturn
