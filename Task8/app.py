# Environment needs to pip install jsonify, Flask, requests, python-dotenv
from flask import Flask, jsonify
from functions import getData
import random

app = Flask(__name__)

# Default route
@app.route('/')
def index():
    return jsonify({"message": "use: /year to get the data"})

# Data route
@app.route('/<year>', methods=['GET'])
def getItems(year):
    fetchMoviesMade = getData("movies", year).get("total_results")
    fetchEvents = getData("events", year)
    randomEvents = random.sample(fetchEvents, min(4, len(fetchEvents)))
    return jsonify({"Amount of movies released": fetchMoviesMade, "4 Major events": randomEvents})

if __name__ == '__main__':
    app.run(debug=True)
