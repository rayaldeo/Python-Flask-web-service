#!flask/bin/python
from flask import Flask, jsonify, abort,make_response,request, render_template

app = Flask(__name__)

def handle_data(a,b):
        aa = str(a + b)
        return aa

@app.route('/hello', methods=['GET'])
def display_message():
    return "Hello World!"

@app.route('/hello<string:name>', methods=['GET'])
def greet_message(name):
    return "Hello "+name+"!"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'You are trying to access a page that does not exist. :('}),404)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/handle_data', methods=['POST', 'GET'])
def showSolution():
    if request.method == 'POST':
        try:
            a=float(request.form['fnumber'])
        except:
            a=0
            print("This isn't a float!")
        try:
            b=float(request.form['snumber'])
        except:
            b=0
            print("This isn't a float!")
    return render_template('solution.html',solution=str(handle_data(a,b)))

#Rest Call to add two numbers again
@app.route('/handle_data/rest/<int:a>&<int:b>', methods=['GET'])
def performRestCall(a,b):
    try:
        a=float(a)
    except:
        a=0
        print("This isn't a float!")
    try:
        b=float(b)
    except:
        b=0
        print("This isn't a float!")
    return render_template('solution.html',solution=str(handle_data(a,b)))

#This code is used for local server testing. Don't need this in the cloud.
if __name__ == '__main__':
    app.run(debug=True)

