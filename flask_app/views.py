from flask import render_template, flash, redirect, url_for

from flask_app import app, db


@app.route("/")
def index():
    return "<h1>Hello, world!</h1>"
