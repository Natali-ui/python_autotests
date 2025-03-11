import requests

URL = 'https://api.pokemonbattle.ru/v2' 
TOKEN = 'da4871b8dd4f70d0d743017c86ae25c5'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}

body_create_pokemon = {
    "name": "Бульбазаврик",
    "photo_id": 567
}

body_change_name = {
    "pokemon_id": "259900",
    "name": "Kikozavr",
    "photo_id": 567
}

body_pokemon_add_pokeball = {
    "pokemon_id": "259900"
}


'''response_create_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
print(response_create_pokemon.text)'''

'''respons_change_name = requests.put(url= f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(respons_change_name.text)'''

respons_pokemon_add_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokemon_add_pokeball)
print(respons_pokemon_add_pokeball.text)