from flask import render_template
from app import app
from models.events import *

@app.route("/events")
def index():
    return render_template("index.html", title="events", events=events)