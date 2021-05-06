from flask 
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', title='Welcome', members=users)


@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/', methods=['GET'])
def fortune():
    content = "" 
    os.system("fortune >> fortune.txt")
    with open("fortune.txt", "r") as f:
        content = f.read()
        content = "<pre>" + content + "</pre>"
    os.system("rm -rf fortune.txt")
    return content

@app.route('/cowsay/<string:message>/', methods=['GET'])
def cowsay(message):
    content = ""
    os.system("cowsay " + message + " >> cowsay.txt")
    with open("cowsay.txt", "r") as f:
        content = f.read()
        content = "<pre>" + content + "</pre>"
    os.system("rm -rf cowsay.txt")
    return content


@app.route('/cowfortune/', methods=['GET'])
def cowfortune():
    outcontent = ""
    # cowsay stuff
    os.system("cowsay `fortune` >> cowsay.txt")
    with open("cowsay.txt", "r") as f:
        outcontent = f.read()
        outcontent = "<pre>" + outcontent + "</pre>"
    os.system("rm -rf cowsay.txt")

    return outcontent
