import os
import dotenv
import bcrypt
import datetime
from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import FlaskLoginClient, login_manager, UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db' # temp code fill in with database uri
db = SQLAlchemy(app)


# TODO classes for user's coins
# TODO classes for user's # of events completed

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    leaderboard_entries = db.relationship('LeaderboardEntry', backref='user', lazy=True)

class LeaderboardEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    date_updated = db.Column(db.DateTime, default=datetime.datetime, nullable=False)

@app.route('/')
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
       username = request.form.get("username")
       password = request.form.get("password") 
       if not validate_on_submit(username, password):
           return None # if not valid redirct with error
    return render_template("login.html")

def validate_on_submit(username, password):
    error = None
    if not username.isalnum():
        error = False
        return error

@app.route("/register", methods=["POST", "GET"])
def register():
    return redirect(url_for("register"))

@app.route("/home", methods=["POST", "GET"])
def events():
    return redirect(url_for("home"))

@app.route("/leaderboard", methods=["POST", "GET"])
def leaderboard():
    return redirect(url_for("leaderboard"))