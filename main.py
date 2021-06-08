from flask import Blueprint, request, render_template
from werkzeug.utils import escape
from __init__ import db
from __init__ import pymongo

main = Blueprint('main', __name__)

@main.route('/')
def Index():
    last_data = db.datosMapa.find_one({},sort=[( '_id', pymongo.DESCENDING )])
    return render_template("pages/index.html",page_title='COVIDMX',data=last_data)
