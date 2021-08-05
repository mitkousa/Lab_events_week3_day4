from flask import render_template, request
from app import app
from models.events import *
from models.event_class import *

@app.route("/events")
def index():
    return render_template("index.html", title="events", events=events)

@app.route("/events/newevent")
def new_event():
    return render_template("new_event.html", title="newevent")

@app.route("/events", methods=["POST"])
def add_event():
    event_date=request.form["date"]
    event_name=request.form["event_name"]
    event_guest_number=request.form["number_of_guests"]
    event_room_name=request.form["room_name"]
    event_description=request.form["description"]
    new_event=Event(event_date, event_name, event_guest_number, event_room_name, event_description)
    add_new_event(new_event)
    return render_template("index.html", title="events", events=events)
