from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)


# Home Route
@app.route("/")
def show_form():
    """Shows form to input story words"""
    return render_template("home.html")


# Story Route (handle form submission)
@app.route("/story")
def show_story():
    """Shows the resulting story for madlib answers"""
    madlib = story.generate(request.args)
    return render_template("story.html", story=madlib)
