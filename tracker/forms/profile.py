from flask_wtf import Form
from wtforms import validators
from wtforms.fields import SelectField, TextAreaField, IntegerField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email, regexp
from tracker.models.user import User


class UserProfileForm(Form):
    """Form to enter edit user profile."""

    username = StringField(label=u'Username', validators=[InputRequired()])
    first_name = StringField(label=u'First Name', validators=[InputRequired()])
    last_name = StringField(label=u'Last Name', validators=[InputRequired()])
    email = EmailField(label=u'Email', validators=[InputRequired("Please enter your email address.")])
