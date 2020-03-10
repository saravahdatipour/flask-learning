from flask import Flask, request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    # response = "Request Context<br>"
    # response += f"Request Method : {request.method}<br>"
    # response += f"Request Args:{request.args}<br>"
    # response += f"Request Body/Data :{request.form}<br>"
    name = request.args.get('name') or request.form.get('name')
    # the or function will choose whichever that is first and TRUE or is TRUE

    return f"HELLO {name}"