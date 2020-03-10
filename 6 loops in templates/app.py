from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    students = ['sara','farzam','ali']
    numbers = [i for i in range(20)]
    return render_template("index.html",students=students, numbers = numbers)