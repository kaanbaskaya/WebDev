from db import db
from datetime import date, datetime

class University(db.Model):
    __tablename__ = 'university'
    uni_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    short_name = db.Column(db.Text)
    location = db.Column(db.Text)

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    uni_id = db.Column(db.Integer, db.ForeignKey('university.uni_id'))
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.Date, default=date.today)
    profile_picture = db.Column(db.LargeBinary, nullable=False)
    description = db.Column(db.Text, nullable=False, default="")

    university = db.relationship('University', backref='students', lazy=True)
    personality_result = db.relationship('PersonalityResult', uselist=False, backref='user')

class PersonalityResult(db.Model):
    __tablename__ = 'personality_result'
    result_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), unique=True)
    vec_ei = db.Column(db.Float)
    vec_sn = db.Column(db.Float)
    vec_tf = db.Column(db.Float)
    vec_jp = db.Column(db.Float)
    mbti_type = db.Column(db.Text)
    completed_at = db.Column(db.Date)

class Swipe(db.Model):
    __tablename__ = 'swipe'
    swipe_id = db.Column(db.Integer, primary_key=True)
    swiper_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    swiped_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    swipe_type = db.Column(db.Text)  # e.g., 'like' or 'dislike'
    swiped_at = db.Column(db.Date)

class Match(db.Model):
    __tablename__ = 'match'
    match_id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    user2_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    compatibility = db.Column(db.Float)
    status = db.Column(db.Text)  # e.g., 'pending', 'accepted'
    matched_at = db.Column(db.Date)

    #hier damit dei Möglichkeit besteht ein Match zu bewerten
    evaluated_by_user1 = db.Column(db.Boolean, default=False)
    evaluated_by_user2 = db.Column(db.Boolean, default=False)
    rating_by_user1 = db.Column(db.Integer)
    rating_by_user2 = db.Column(db.Integer)

    user1 = db.relationship('User', foreign_keys=[user1_id], backref='matches_as_user1')
    user2 = db.relationship('User', foreign_keys=[user2_id], backref='matches_as_user2')

class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('match.match_id'), nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now) #<= automatisch aktuelle Zeit

    sender = db.relationship('User', backref='sent_messages')