from knust import db, login_manager
from knust import bcrypt
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    f_name = db.Column(db.String(length=30), nullable=False)
    s_name = db.Column(db.String(length=30), nullable=False)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    student_id = db.Column(db.String(length=8), nullable=False, unique=True)
    index_no = db.Column(db.String(length=12), nullable=False, unique=True)
    course = db.Column(db.String(length=30), nullable=False)
    contact = db.Column(db.String(length=10), nullable=False, unique=True)
    cwa = db.Column(db.Integer, nullable=False, default=100)
    year = db.Column(db.Integer, nullable=False, default=1)
    result = db.relationship('Result', backref='owned_user', lazy=True)
    post = db.relationship('Posts', backref='owned_user', lazy=True)
    comment = db.relationship('Comments', backref='owned_user', lazy=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def __repr__(self):
        return '<User %r>' % self.name

class Result(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    index_no = db.Column(db.String(length=12), nullable=False)
    subject = db.Column(db.String(length=60), nullable=False)
    credit = db.Column(db.Integer(), nullable=False)
    mid_score = db.Column(db.Integer(), nullable=False)
    exam_score = db.Column(db.Integer(), nullable=False)
    total = db.Column(db.Integer(), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'CWA {self.cwa}'

class Posts(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    #author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #created = db.Column(db.Timestamp, nullable=False, default=current_timestamp)
    created = db.Column(db.DateTime, unique=True, default=datetime.utcnow)
    title = db.Column(db.String(length=60), unique=True, nullable=False)
    body = db.Column(db.String(length=60), unique=True, nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % self.name

class Comments(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    #author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #created = db.Column(db.Timestamp() , nullable=False, default=current_timestamp)
    created = db.Column(db.DateTime, unique=True, default=datetime.utcnow)
    body = db.Column(db.String(length=60), unique=True, nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Comment %r>' % self.name

#class Role(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(64), unique=True)
#    default = db.Column(db.Boolean, default=False, index=True)
#    permissions = db.Column(db.Integer)
#    users = db.relationship('User', backref='role', lazy='dynamic')