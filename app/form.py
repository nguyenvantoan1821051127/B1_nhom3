from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo, InputRequired
from app.models import User


class signUpForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(
        min=6, message=('Your password is too short.'))])
    rePassword = PasswordField('reType Password', validators=[
                               DataRequired(), EqualTo('password', message='Passwords must match')])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_passengerId(self, password):
        password = User.query.filter_by(password=password.data).first()
        if password is not None:
            raise ValidationError(
                'username has been already used! Please use a different username.')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError(
                'email has been already used! Please use a different email.')


class loginForm(FlaskForm):
    name = StringField('Full Name ', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')


class addTeacher(FlaskForm):
    fullname = StringField('Full Name', validators=[DataRequired()])
    gender = RadioField('male')
    gender = RadioField('female')
    phone = StringField('Phone ', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Sign Up')
