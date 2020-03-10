import random
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/results/')
def result():
    
    headsOrTails=random.randint(1,2)

    return render_template("results.html",headsOrTails=headsOrTails)