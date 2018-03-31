from flask import Flask, render_template
app = Flask(__name__)
import csv

app.config['TEMPLATES_AUTO_RELOAD'] = True

def read_csv():
    file = open('rcships.csv', 'r')
    return list(csv.DictReader(file))


@app.route('/')
def index():
    all_ships = read_csv()
    return render_template('index.html', vessels = all_ships)

@app.route('/ship/<ship_id>')
def ship(ship_id):
    all_ships = read_csv()
    for ship in all_ships:
        if ship['ID'] == ship_id:
            return render_template('ship.html', ship = ship)

if __name__ == '__main__':
    app.run(debug=True)
