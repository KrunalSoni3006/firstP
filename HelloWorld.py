from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 's\x84j\x9c\xbaZpr\x89\xf5\xfa\xd5\xe8M\x9e j\x9c\xa6\xf2\xc1\xfe~\x83'

bookmark = []


def store_bookmark(url):
    bookmark.append(dict(url=url, date=datetime.utcnow()))


@app.route("/")
def hello():
    return render_template('index.html', title='This is my title',
                           detail="This is from details....!!!")


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmark(url)
        flash("please find below list of URLs.")
        flash("Bookmark is :- '{}'".format(url))
        return redirect(url_for('hello'))
    return render_template('Add.html')
