from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wall.db"

###Setting up the database and the fields
db = SQLAlchemy(app)
class wall(db.Model):
    id=db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(25), nullable=False)
    content = db.Column(db.Text, nullable=False, default="N/A")
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


###the pages

#the main profile page
@app.route("/")
def index():
    return render_template("index.html")

#the portfolio page
@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")
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
        return render_template("wall.html", theWall=allPosts)

#deleting posts
@app.route("/wall/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    post = wall.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect("/wall")

#projects page
@app.route("/projects")
def projects():
    return render_template("projects.html")



##running the app
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
