from crypt import methods
from flask import Flask
from flask import render_template, request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

app = Flask(__name__)
# blog.dbという名前のデータベースを作成している。
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(300), nullable=False)
    create_at = db.Column(db.DateTime, nullable=False , default=datetime.now(pytz.timezone("Asia/Tokyo")))

@app.route("/", methods=["POST", "GET"])
def hello():
    if request.method == "GET":
        posts = Post.query.all()
        return render_template("index.html",posts=posts)
        
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        post = Post(title=title,body=body)
        db.session.add(post)
        db.session.commit()
        return redirect("/")

    else:
        return render_template("create.html")
