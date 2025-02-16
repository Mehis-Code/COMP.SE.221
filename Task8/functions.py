# Functions to get data
from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY_A")
API_KEY2 = os.getenv("API_KEY_B")

def getData(api_type, year):
    if api_type == "movies":
        url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&page=1&primary_release_year={year}&sort_by=popularity.desc"
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "accept": "application/json"
        }
    elif api_type == "events":
        url = f"https://api.api-ninjas.com/v1/historicalevents?year={year}"
        headers = {
            'X-Api-Key': f'{API_KEY2}'
        }
    else:
        return None

    response = requests.get(url, headers=headers).json()
    return response