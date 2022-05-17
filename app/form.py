from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, RadioField, FloatField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo, InputRequired, NumberRange
from app.models import User


# ----------Toàn----------


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

# ----------Việt----------


class FormUpdateTranscripts(FlaskForm):
    score_C = FloatField(
        "Điểm C",
        validators=[
            DataRequired(),
            NumberRange(
                min=0, max=10, message="Vui lòng nhập giá trị của điểm từ 0 đến 10"
            ),
            # Length(max=3),
        ],
        render_kw={"step": "0.1"},
    )
    score_B = FloatField(
        "Điểm B",
        validators=[
            DataRequired(),
            NumberRange(
                min=0, max=10, message="Vui lòng nhập giá trị của điểm từ 0 đến 10"
            ),
            # Length(max=3),
        ],
        render_kw={"step": "0.1"},
    )
    score_A = FloatField(
        "Điểm A",
        validators=[
            DataRequired(),
            NumberRange(
                min=0, max=10, message="Vui lòng nhập giá trị của điểm từ 0 đến 10"
            ),
            # Length(max=3),
        ],
        render_kw={"step": "0.1"},
    )
    submit = SubmitField("Xác nhận")

    # Valtdate các điểm khi submit
    def validate_score_C(self, score_C):
        score_C = float(score_C.data)
        if score_C < 0 or score_C > 10:
            raise ValidationError("Vui lòng nhập giá trị của điểm từ 0 đến 10")

    def validate_score_B(self, score_B):
        score_B = float(score_B.data)
        if score_B < 0 or score_B > 10:
            raise ValidationError("Vui lòng nhập giá trị của điểm từ 0 đến 10")

    def validate_score_A(self, score_A):
        score_A = float(score_A.data)
        if score_A < 0 or score_A > 10:
            raise ValidationError("Vui lòng nhập giá trị của điểm từ 0 đến 10")
