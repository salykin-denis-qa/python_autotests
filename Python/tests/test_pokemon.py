import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '8cef290e66c87611e92cf626c0494f0b'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '2603'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID} )
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID} )
    assert response_get.json()["data"][0]["trainer_name"] =='Денис'

