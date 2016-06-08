from flask_wtf import Form
from wtforms import TextField, validators
from wtforms.validators import InputRequired
from wtforms.fields import IntegerField
from wtforms.fields import SelectMultipleField
from wtforms import widgets


class ContactForm(Form):
    """ContactForm."""
    email = TextField(label=u'Email Address', validators=[InputRequired()])
