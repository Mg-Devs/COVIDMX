from re import search
from bson.objectid import ObjectId
from flask import Blueprint, request, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user, login_user, logout_user
from pymongo import message
from datetime import date

from werkzeug.utils import escape
from models import User
from app import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = 'check' in request.form

        user = db.userAuth.find_one({'email':email})
        if not user or not check_password_hash(user['password'], password):
            flash("El correo o la contraseña son incorrectos")
            return redirect(url_for("auth.login", page_title='Ingresa | COVIDMX'))
        else:
            login_user(User(user),remember=remember)
            return redirect(url_for('auth.home'))
    else:
        return render_template("pages/login.html", page_title='Ingresa | COVIDMX')

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
            flash("El nombre de usuario ya existe, elige otro")
            return redirect(url_for("auth.register", page_title='Registrate | COVIDMX'))
        if existsE > 0:
            flash("El correo ya fue registrado en nuestra base de datos")
            return redirect(url_for("auth.register", page_title='Registrate | COVIDMX'))
        
        user = {"user_nickname":nickname,"user_firstname": name, "user_lastname": lastname, "email": email, "password": generate_password_hash(password)}
        db.userAuth.insert_one(user)

        return redirect(url_for('auth.login', page_title='Ingresa | COVIDMX'))
    else:
        return render_template("pages/register.html", page_title='Registrate | COVIDMX')

@auth.route('/home')
@login_required
def home():
    posts = db.posts.find()
    print(posts)
    return render_template("pages/home.html", page_title='COVIDMX', user=current_user, posts=posts)

@auth.route('/new-post', methods=['GET', 'POST'])
@login_required
def npost():
    if request.method == 'POST':

        title = request.form.get('title')
        desc = request.form.get('desc')
        content = request.form.get('content')
        author = current_user.user_json.get("user_nickname")
        creation_date = date.today()
        
        post = {"title":title,"desc": desc, "content": content, "author":author, "creation_date":str(creation_date), "views":0}
        db.posts.insert_one(post)

        return redirect(url_for('auth.home'))
    else:
        return render_template("pages/npost.html", page_title='Nuevo Post | COVIDMX',  user=current_user)

@auth.route('/post/<postId>')
@login_required
def view_post(postId):
    post = db.posts.find_one({'_id':ObjectId(escape(postId))})
    return render_template("pages/post.html", page_title='COVIDMX', post=post, user=current_user)


@auth.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'POST':

        search = request.form.get('searchInput')
        search = '\W*((?i)'+search+'(?-i))\W*'
        print(search)
        posts = db.posts.find({ '$or': [{'title':{'$regex':search}},{'desc':{'$regex':search}},{'content':{'$regex':search}}]})
    else:
        posts = db.posts.find()

    
    print(posts)
    return render_template("pages/home.html", page_title='COVIDMX', user=current_user, posts=posts)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.Index'))