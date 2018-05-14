from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import os

from forms import BookmarkForm
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 's\x84j\x9c\xbaZpr\x89\xf5\xfa\xd5\xe8M\x9e j\x9c\xa6\xf2\xc1\xfe~\x83'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'firstP.db')

db=SQLAlchemy(app)

bookmark = []


def new_bookmarks(num):
    return sorted(bookmark, key=lambda bm: bm['date'], reverse=True)[:num]


def store_bookmark(url, description):
    bookmark.append(dict(
        url=url,
        date=datetime.utcnow(),
        description="description"
    ))


@app.route("/")
def hello():
    return render_template('index.html', title='This is my title',
                           detail="This is from details....!!!", new_bookmarks=new_bookmarks(5))


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        # url = request.form['url']
        # store_bookmark(url)
        url = form.url.data
        description = form.description.data
        store_bookmark(url, description)
        flash("please find below list of URLs.")
        flash("Bookmark is :- '{}'".format(url))
        return redirect(url_for('hello'))
    return render_template('Add.html', form=form)
