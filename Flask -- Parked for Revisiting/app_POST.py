from flask import Flask, request
from flask import render_template, jsonify

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def home_page():
    return render_template("index.html")

@app.route("/math", methods = ['POST'])
def math_ops():
    if (request.method == 'POST'):
        drop_down_val =  request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        if drop_down_val == 'add':
            result = f"The sum of {num1} and {num2} is : {num1+num2}"
        
        if drop_down_val == 'subtract':
            result = f"The subtraction of {num1} and {num2} is : {num1-num2}"

        if drop_down_val == 'multiply':
            result = f"The product of {num1} and {num2} is : {num1*num2}"
        
        if drop_down_val == 'divide':
            result = f"The divison of {num1} and {num2} is : {num1/num2}"
        
        
        return render_template('results.html' , result = result)



if __name__ == "__main__":
    app.run(host = "0.0.0.0")