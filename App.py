from flask import Flask, render_template
from flask import request
from dotenv import dotenv_values
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
config = dotenv_values(".env")

client = MongoClient(config.get("DB_URL"))
db = client.covidmx

@app.route('/')
def Index():
    last_data = db.datosMapa.find_one({},sort=[( '_id', pymongo.DESCENDING )])
    print(last_data)
    return render_template("pages/index.html",page_title='COVIDMX',data=last_data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "GG"
    else:
        return render_template("pages/login.html",page_title='Ingresa | COVIDMX')

@app.route('/singin', methods=['GET', 'POST'])
def singin():
    if request.method == 'POST':
        return "GG"
    else:
        return render_template("pages/singin.html",page_title='Registrate | COVIDMX')

if __name__ == '__main__':
    app.run(port=8080, debug=True)