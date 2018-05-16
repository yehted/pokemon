from flask import Blueprint, jsonify
import requests

bp = Blueprint('api', __name__)

BASE_URL = "http://pokeapi.co/api/v2"

@bp.route('/')
def home():
    return "Hello world!"

@bp.route('/pokemon/<pokemon_id>')
def overview(pokemon_id):
    r = requests.get(BASE_URL + '/pokemon/{}'.format(pokemon_id))
    r.raise_for_status()

    return jsonify(r.json())

@bp.route('/move/<move_id>')
def attack(move_id):
    r = requests.get(BASE_URL + '/move/{}'.format(move_id))
    r.raise_for_status()

    return jsonify(r.json())
