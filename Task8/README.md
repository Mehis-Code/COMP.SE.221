Service that fetches data from 2 API:s, according to course task 8<br />
Uses https://developer.themoviedb.org/reference/intro/getting-started (MovieDB-API) for amount of movies
Uses https://www.api-ninjas.com/api/historicalevents (Api-Ninjas-API) for 4 random historical events

REQUIRES:<br />
Environment requires installing Flask, python-dotenv, requests and jsonify with pip.<br />
Need .env file with an API_KEY_A for MovieDB and API_KEY_B for Api-ninjas<br />

RUN WITH:<br />
export FLASK_APP=ms.py<br />
flask run
