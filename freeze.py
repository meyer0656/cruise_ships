from flask_frozen import Freezer
# instead of routes, use the name of the file that runs YOUR Flask app
from ships_app import app
import csv

app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

@freezer.register_generator
def ship():
    for ship in ship:
        yield {'ship_id': vessels.id}

if __name__ == '__main__':
    freezer.freeze()
