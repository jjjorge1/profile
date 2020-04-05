from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.sqlite3"

###Setting up the database and the fields
db = SQLAlchemy(app)
class wall(db.Model):
    id=db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(25), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)


##the pages
@app.route("/")
def index():
    return render_template("index.html")
