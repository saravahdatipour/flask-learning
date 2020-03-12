from flask import Flask , render_template,request
from forms import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfghjk'

@app.route('/')

def index():
    login_form = LoginForm()

    return render_template('index.html',login_form=login_form)

@app.route('/login',methods=['POST'])
def login():
    login_form = LoginForm(request.form)
    if not login_form.validate_on_submit():
        return "Error"
    return "OK"
    