import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '8cef290e66c87611e92cf626c0494f0b'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}


body_create = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_rename = {
    "pokemon_id": '27966',
    "name": "Пикачу",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_add_pokebal = {
    "pokemon_id": '27966'
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)

response_add_pokebal = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokebal)
print(response_add_pokebal.text)