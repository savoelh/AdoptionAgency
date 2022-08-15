from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField
from wtforms.validators import URL, optional, AnyOf, NumberRange, DataRequired

class AddPetForm(FlaskForm):

    name = StringField("Pet Name:", validators=[DataRequired(message='Your pet must have a name')])
    species = StringField("Species:") #Tried to use AnyOf to limit the selections, but got a lot of weird errors
    photo_url = StringField("Photo:", validators=[optional(), URL(require_tld=True, message="Please enter a valid url")]) 
    age = IntegerField("Age:", validators=[NumberRange(min=1, max=30, message="Must enter a number between 1-30")])
    notes = StringField("Additional information:")
    

class EditPetForm(FlaskForm):

    photo_url = StringField("Photo:", validators=[optional(), URL(require_tld=True, message="Please enter a valid url")])
    notes = StringField("Additional information:")
    available = BooleanField("This pet is available for adoption:") 
