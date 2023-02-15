from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flightinfo', methods=['POST'])
def flightinfo():
    airline_code = request.form['airline_code']
    flight_number = request.form['flight_number']
    year = request.form['year']
    month = request.form['month']
    day = request.form['day']
    url = f"https://api.airline.com/flightinfo/{airline_code}/{flight_number}/{year}/{month}/{day}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        origin = data['origin']
        destination = data['destination']
        departure_time = data['departure_time']
        arrival_time = data['arrival_time']
        duration = data['duration']
        return render_template('flightinfo.html', airline_code=airline_code, flight_number=flight_number, year=year, month=month, day=day, origin=origin, destination=destination, departure_time=departure_time, arrival_time=arrival_time, duration=duration)
    else:
        return "API request failed"

if __name__ == '__main__':
    app.run(debug=True)
