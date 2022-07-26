
from datetime import datetime
from flask import Flask, render_template


app = Flask("hello")

posts = [
    {
        "title" : "Meu Primeiro Post",
        "body" : "Este é o corpo do texto",
        "author" : "Wesllei",
        "created" : datetime(2022,7, 26, 0, 0)
    },
    {
        "title" : "Meu Segundo Post",
        "body" : "Este é o corpo do texto",
        "author" : "Wesllei",
        "created" : datetime(2022,7, 26, 0, 0)
    },
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)
