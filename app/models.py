from . import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    attendees = db.relationship("Attendee", backref="event", lazy=True)
    tasks = db.relationship("Task", backref="event", lazy=True)

class Attendee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"), nullable=True)
    tasks = db.relationship("Task", backref="attendee", lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    deadline = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default="Pending")
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"), nullable=False)
    attendee_id = db.Column(db.Integer, db.ForeignKey("attendee.id"), nullable=True)
