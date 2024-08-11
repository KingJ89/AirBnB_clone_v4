#!/usr/bin/python3
"""Initiates a Custom Flask Web Application."""
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid

# Initialize Flask application
app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    """Closes the active SQLAlchemy session."""
    storage.close()

@app.route('/0-hbnb/', strict_slashes=False)
def display_hbnb():
    """Displays the HBNB page."""
    state_objects = storage.all(State).values()
    sorted_states = sorted(state_objects, key=lambda state: state.name)

    states_with_cities = [
        (state, sorted(state.cities, key=lambda city: city.name))
        for state in sorted_states
    ]

    amenity_objects = storage.all(Amenity).values()
    sorted_amenities = sorted(amenity_objects, key=lambda amenity: amenity.name)

    place_objects = storage.all(Place).values()
    sorted_places = sorted(place_objects, key=lambda place: place.name)

    cache_id = uuid.uuid4()

    return render_template('0-hbnb.html',
                           states=states_with_cities,
                           amenities=sorted_amenities,
                           places=sorted_places,
                           cache_id=cache_id)

if __name__ == "__main__":
    """Runs the Flask application."""
    app.run(host='0.0.0.0', port=5000)

