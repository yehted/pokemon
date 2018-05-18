import logging
import requests
from flask import Blueprint, jsonify, request

from .battle import RandomBattle
from .pokemon import Pokemon
from .moves import Move

bp = Blueprint('api', __name__)

BASE_URL = "http://pokeapi.co/api/v2"

@bp.route('/')
def home():
    return "Hello world!"

@bp.route('/pokemon/<pokemon_id>', methods=['GET'])
def overview(pokemon_id):
    pokemon = Pokemon(url=BASE_URL + '/pokemon/{}'.format(pokemon_id))
    result = pokemon.pokemon_info

    return jsonify(result)

@bp.route('/move/<move_id>', methods=['GET'])
def attack(move_id):
    move = Move(BASE_URL + '/move/{}'.format(move_id))
    result = move.full_obj

    return jsonify(result)


@bp.route('/battle', methods=['POST'])
def battle():
    """ Expects post data to be application/JSON

    {
        "contestants": [ pokemon_id1, pokemon_id2 ]
    }

    """

    data = request.get_json()
    contestant_1 = data['contestants'][0]
    contestant_2 = data['contestants'][1]

    pokemon_1 = Pokemon(url=BASE_URL + '/pokemon/{}'.format(contestant_1))
    pokemon_2 = Pokemon(url=BASE_URL + '/pokemon/{}'.format(contestant_2))

    random_battle = RandomBattle(pokemon_1, pokemon_2)
    rounds, winner = random_battle.go(power_percent=0.1)
    result = {
        'battle_history': rounds,
        'winner': winner
    }

    return jsonify(result)
