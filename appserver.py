from flask import Flask, render_template, request, session, redirect, url_for, jsonify, abort
import os
import subprocess
import uuid 

app = Flask(__name__)
app.secret_key = str(uuid.uuid4().hex)
intropre = '<pre style="border:black solid 4px; border-radius: 12.5px; background:silver; opacity: 0.65; margin-left:auto; margin-right:auto;height:100%;height:65%;overflow:auto; text-align:center; font-size:16px;">'
@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortunenormal():
    fortune = subprocess.check_output(["fortune"]).decode()
    prereturn = intropre + fortune + "</pre>"
    return prereturn

@app.route('/cowsay/<message>/')
def cowsaynormal(message):
    arg_list = ["cowsay"] + message.split()
    cow= subprocess.check_output(arg_list).decode()
    prereturn = intropre + cow + "</pre>"
    return prereturn

@app.route('/cowfortune/')
def cowsayfortune():
    outcollect = subprocess.check_output(["fortune"]).decode()
    argtodecode = ["cowsay"] + outcollect.split()
    fortunecow = subprocess.check_output(argtodecode).decode()
    prereturn = intropre + fortunecow + "</pre>"
    return prereturn
