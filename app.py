from flask import Flask, render_template, request, url_for, redirect, jsonify
from waitress import serve
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    msg = "Hello World!"
    return render_template('index.html', msg=msg)

@app.route('/data', methods=['GET'])
def get_data():
    try:
        with open('main.json', 'r') as file:
            json_data = json.load(file)
        return jsonify(json_data)
    except Exception as e:
        return str(e)

@app.route('/page',methods=["GET","POST"])
def page():
    json_file='./result.json'
    if request.method == 'POST':
        new_person = {
            "firstName": request.form['firstname'],
            "lastName": request.form['lastname']
        }
        with open(json_file, 'r') as file:
            data = json.load(file)
        data.append(new_person)
        with open(json_file, 'w') as file:
            json.dump(data, file, indent=4)
        return redirect(url_for('page'))
    return render_template('page.html')

@app.route('/result', methods=['GET'])
def result():
    try:
        with open('result.json', 'r') as file:
            json_data = json.load(file)
        return jsonify(json_data)
    except Exception as e:
        return str(e)

serve(app,host='0.0.0.0',port=8080)