from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "e4e1fbafab8cb2decbdbf969f047efea"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City name is required"}), 400
    
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code != 200:
        return jsonify({"error": "City not found"}), 404
    
    data = response.json()
    weather_info = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
    }
    
    return jsonify(weather_info)

if __name__ == '__main__':
    app.run(debug=True)
