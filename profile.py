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


###the pages

#the main profile page
@app.route("/")
def index():
    return render_template("index.html")
#the wall page 
#you can post things and read things and delete things
@app.route("/wall", methods=["GET", "POST"])
def theWall():
    if request.method =="POST":
        postAuthor = request.form["author"]
        postContent = request.form["content"]
        newPost = wall(name=postAuthor, content=postContent)
        db.session.add(newPost)
        db.session.commit()
        return redirect("/wall")
    else:
        allPosts = wall.query.order_by(wall.date).all()
        #i am not to sure about the "posts=allPosts"
        return render_template("wall.html", posts=allPosts)


##running the app
if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)
