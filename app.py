"""Flask app for adopt app."""

import os
from forms import AddPet
from flask import Flask, request, render_template, session, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

# API_SECRET_KEY = os.environ['API_SECRET_KEY']

app = Flask(__name__)

app.config['SECRET_KEY'] = 'API_SECRET_KEY'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def load_homepage():
    """Load homepage that shows all the pets."""
    pets = Pet.query.all()

    return render_template('homepage.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Pet add form; handle adding"""

    form = AddPet()

    if form.validate_on_submit():

        name = form.name.data.title()
        species = form.species.data.title()
        photo_url = form.photo_url.data
        age = form.age.data.title()
        notes = form.notes.data

        pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes
        )

        db.session.add(pet)
        db.session.commit()

        flash(f"Added {pet.name}!")
        return redirect('/add')
    else:
        return render_template('add_pet_form.html', form=form)


@app.route('/<int:id>', methods=['GET', 'POST'])
def display_edit_pet_form(id):
    """Show pet info with edit form; Handle edit"""

    pet = Pet.query.get_or_404(id)
    form = AddPet(obj=pet)

    if form.validate_on_submit():

        pet.name = form.name.data.title()
        pet.species = form.species.data.title()
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data.title()
        pet.notes = form.notes.data

        db.session.commit()
        flash(f"{pet.name} information has been updated")
        return redirect(f'/{id}')

    else:
        return render_template('pet_details.html', pet=pet, form=form)
