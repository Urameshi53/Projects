from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from knust.models import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! please try again')
    username = StringField(label='Username', validators=[Length(min=2, max=30), DataRequired()])
    f_name = StringField(label='First name', validators=[Length(min=2, max=30), DataRequired()])
    s_name = StringField(label='Last name', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address', validators=[Email(), DataRequired()])
    student_id = StringField(label='Student ID', validators=[Length(min=8), DataRequired()])
    index_no = StringField(label='Index Number', validators=[Length(min=7), DataRequired()])
    course = StringField(label='Programme', validators=[Length(min=3, max=30), DataRequired()])
    contact = StringField(label='Phone number', validators=[Length(min=10), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create account')

class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField(label='Sign in')

class PostForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    body = TextAreaField(label='Body', validators=[DataRequired()])
    submit = SubmitField(label='Submit', validators=[DataRequired()])

class CommentForm(FlaskForm):
    body = StringField(label='Comment', validators=[DataRequired()])
    submit = SubmitField(label='Submit', validators=[DataRequired()])
    