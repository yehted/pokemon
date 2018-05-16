import logging
import requests
from flask import Blueprint, jsonify, request

from .battle import Battle
from .moves import Moves

bp = Blueprint('api', __name__)

BASE_URL = "http://pokeapi.co/api/v2"

def get_pokemon_info(pokemon_id):
    logging.info("Retrieving info for pokemon: {}".format(pokemon_id))
    r = requests.get(BASE_URL + '/pokemon/{}'.format(pokemon_id))
    r.raise_for_status()

    return r.json()

@bp.route('/')
def home():
    return "Hello world!"

@bp.route('/pokemon/<pokemon_id>', methods=['GET'])
def overview(pokemon_id):
    result = get_pokemon_info(pokemon_id)

    return jsonify(result)

@bp.route('/move/<move_id>', methods=['GET'])
def attack(move_id):
    result = Moves.get_from_move_url(BASE_URL + '/move/{}'.format(move_id))

    return jsonify(result)


@bp.route('/battle', methods=['POST'])
def battle():
    """ Expects post data to be JSON

    {
        "contestants": [ pokemon_id1, pokemon_id2 ]
    }

    """

    data = request.get_json()
    pokemon_1 = data['contestants'][0]
    pokemon_2 = data['contestants'][1]

    pokemon_1_info = get_pokemon_info(pokemon_1)
    pokemon_2_info = get_pokemon_info(pokemon_2)

    pokemon_battle = Battle(pokemon_1_info, pokemon_2_info)
    battle_history, winner =  pokemon_battle.execute()
    result = {
        'battle_history': battle_history,
        'winner': winner
    }

    return jsonify(result)
