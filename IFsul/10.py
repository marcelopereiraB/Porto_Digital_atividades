from flask import Flask, render_template, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask("hello")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(70), nullable=False)
    body = db.Column(db.String(500))
    author = db.Column(db.String(20))
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)

db.create_all()

@app.route("/")
def index():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)

@app.route("/populate")
def populate():
    post1 = Post(title="Post 1", body="Texto do Post", author="Feulo")
    post2 = Post(title="Post 2", body="Texto do Post 2", author="Feulo")
    db.session.add(post1)
    db.session.add(post2)
    db.session.commit()
    return redirect("/")
