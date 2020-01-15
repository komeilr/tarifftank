from flask_wtf import FlaskForm
from wtforms import validators, TextAreaField, StringField, SubmitField

class BlogForm(FlaskForm):
    title = StringField('title', )