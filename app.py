from datetime import datetime
from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask("hello")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key= True, autoincrement= True)
    title = db.Column(db.String(70), nullable= False)
    body = db.Column(db.String(500))
    created = db.Column(db.DateTime, nullable= False, default= datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key= True, autoincrement= True)
    username = db.Column(db.String(20), nullable= False, unique = True, index = True)
    email = db.Column(db.String(64), nullable= False, unique = True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship(Post, backref="author")
    
    
db.create_all()

@app.route("/")
def index():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)

@app.route("/populate")
def populate():
    user = User(username= "Wesllei", email = "wesllei@gmail.com", password_hash = "a")
    post1 = Post(title="Titulo post 1", body="texto do post 1", author=user)
    post2 = Post(title="Titulo post 2", body="texto do post 2", author=user)
    db.session.add(user)
    db.session.add(post1)
    db.session.add(post2)
    db.session.commit()
    return redirect(url_for("index"))
    
    
@app.route("/login")
def login():
    return render_template("login.html")
           
