#Environment needs to pip install jsonify, Flask, requests, python-dotenv
from flask import Flask, jsonify, request
import requests
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)
API_KEY = os.getenv("API_KEY_3")

#Function to get the chosen weather
def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(url)
    return response.json()

#Default route
@app.route('/')
def index():
    return jsonify({"message": "use: /cityname to get the weather"})

#Weather route
@app.route('/<city>', methods=['GET'])
def weatherGet(city):
    setData = get_weather(city)

    #Error msg if city not found
    if "error" in setData:
        return jsonify(setData), 404
    
    return jsonify(setData)

if __name__ == '__main__':
    app.run(debug=True)