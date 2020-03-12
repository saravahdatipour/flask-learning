from flask import Flask,render_template,request

app = Flask(__name__)

auth = {'username':'sara','password':'1234'}

@app.route('/',methods=['POST','GET'])
def index():
    return render_template("index.html")
@app.route('/login',methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if password is None:
        return "Error! Where is your Password!?"
    if username == auth['username'] and password == auth['password']:
        return f"welcome {username}!"

    return "Incorrect Username/Password!"