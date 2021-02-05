import requests
import os 
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) 

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': os.getenv('spotify_key'),
    'client_secret': os.getenv('spotify_secret'),

})

auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

BASE_URL = 'https://api.spotify.com/v1/browse/new-releases'

params = {
    'country': 'SE',
    'limit': '10',
    'offset' : '0',
}

response = requests.get(BASE_URL, params = params, headers=headers)
data = response.json()

for i in range(0, 10):
    print(data['albums']['items'][i]['artists'][0]['name'])