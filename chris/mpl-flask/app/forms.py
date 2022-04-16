"""
Forms...
"""

from flask_wtf import FlaskForm
from markupsafe import Markup
from wtforms import (
    FileField,
    SubmitField,
)
from wtforms.validators import DataRequired


class DataForm(FlaskForm):
    upload = FileField("File Upload", validators=[DataRequired()])
    submit_markup = Markup("Upload &#8594;")
    submit = SubmitField(submit_markup)
