from flask 
import os

app = Flask(__name__)

#this is supposed to load an index.html and render

returnvalue = ""
@app.route('/')
def hello():
    return render_template('index.html', title='Welcome', members=users)


@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/', methods=['GET'])
def fortune():
    os.system("fortune >> fortune.txt")
    with open("fortune.txt", "r") as f:
        returnvalue = f.read()
        valueof = "<pre>" + returnvalue + "</pre>"
    os.system("rm -rf fortune.txt")
    returnvalue.close()
    return content

@app.route('/cowsay/<string:message>/', methods=['GET'])
def cowsay(message):
    os.system("cowsay " + message + " >> cowsay.txt")
    with open("cowsay.txt", "r") as f:
        content = f.read()
        content = "<pre>" + content + "</pre>"
    os.system("rm -rf cowsay.txt")
    return content


@app.route('/cowfortune/', methods=['GET'])
def cowfortune():
    # cowsay stuff
    os.system("cowsay `fortune` >> cowsay.txt")
    with open("cowsay.txt", "r") as f:
        outcontent = f.read()
        outcontent = "<pre>" + outcontent + "</pre>"
    os.system("rm -rf cowsay.txt")

    return outcontent
