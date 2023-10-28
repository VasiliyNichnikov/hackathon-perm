from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import FileField

# from app import allowed_files
#
#
# class MediaForm(FlaskForm):
#     file = FileField(validators=[FileAllowed(allowed_files, "Image and videos!")])