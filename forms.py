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
        """ Validate if new pet species is a cat, dog or porcupine
            Raises an error if not one of the above species
        """

        valid_inputs = ('cat', 'dog', 'porcupine')
        if field.data.lower() not in valid_inputs:
            raise ValidationError('Species must be Cat, Dog, or Porcupine')

    def validate_age(form, field):
        """ Validate if new pet age is baby, young, adult, or senior 
            Raises an error if not one of the above ages
        """

        valid_inputs = ('baby', 'young', 'adult', 'senior')
        if field.data.lower() not in valid_inputs:
            raise ValidationError(
                'Species must be Baby, Young, Adult or Senior')
