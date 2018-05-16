import logging
import requests

BASE_URL = "http://pokeapi.co/api/v2"

def get_pokemon_info(pokemon_id):
    logging.info("Retrieving info for pokemon: {}".format(pokemon_id))
    r = requests.get(BASE_URL + '/pokemon/{}'.format(pokemon_id))
    r.raise_for_status()

    return r.json()

def get_move(move_id):
    r = requests.get(BASE_URL + '/move/{}'.format(move_id))
    r.raise_for_status()

    return r.json()

