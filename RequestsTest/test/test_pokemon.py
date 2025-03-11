import pytest
import requests

URL = 'https://api.pokemonbattle.ru/v2' 
TOKEN = 'da4871b8dd4f70d0d743017c86ae25c5'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '23949'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers')
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url=f'{URL}/trainers',params= {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Lila Stitch'

