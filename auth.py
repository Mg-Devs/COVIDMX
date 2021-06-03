from flask import Blueprint, request, render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user
from pymongo import message
from __init__ import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = request.form.get('remember')

        user = db.userAuth.find_one({'email':email})
        if not user or not check_password_hash(user['password'], password):
            return render_template("pages/login.html",page_title='Ingresa | COVIDMX',message="El correo o la contraseña son incorrectos.")
        else:
            #login_user(user,remember=remember)
            return redirect(url_for('auth.home'))
    else:
        return render_template("pages/login.html",page_title='Ingresa | COVIDMX')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        name = request.form.get('name')
        lastname = request.form.get('lastname')
        nickname = request.form.get('nickname')
        email = request.form.get('email')
        password = request.form.get('password')

        existsN = db.userAuth.find({'user_nickname':nickname}).count()
        existsE = db.userAuth.find({'email':email}).count()

        if existsN > 0:
            return render_template("pages/register.html",page_title='Registrate | COVIDMX',message="El nombre de usuario ya existe, elige otro.")
        if existsE > 0:
            return render_template("pages/register.html",page_title='Registrate | COVIDMX',message="El correo ya fue registrado en nuestra base de datos.")
        
        user = {"user_nickname":nickname,"user_firstname": name, "user_lastname": lastname, "email": email, "password": generate_password_hash(password)}
        db.userAuth.insert_one(user)

        return redirect(url_for('auth.login'))
    else:
        return render_template("pages/register.html",page_title='Registrate | COVIDMX')

@auth.route('/home')
def home():
    return render_template("pages/home.html",page_title='COVIDMX')