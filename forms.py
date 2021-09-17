"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import InputRequired, Optional, URL, ValidationError


class AddPet(FlaskForm):
    """Adding Pet Form"""
    name = StringField('Pet Name', validators=[InputRequired()])
    species = StringField('Species', validators=[InputRequired()])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = StringField('Age', validators=[InputRequired()])
    notes = StringField('Notes', validators=[Optional()])

    def validate_species(form, field):
        valid_inputs = ('cat', 'dog', 'porcupine')
        if field.data.lower() not in valid_inputs:
            raise ValidationError('species must be cat, dog, or porcupine')
        
    def validate_age(form, field):
        valid_inputs = ('baby', 'young', 'adult', 'senior')
        if field.data.lower() not in valid_inputs:
            raise ValidationError('species must be baby, young, adult or senior')



