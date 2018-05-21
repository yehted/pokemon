import logging
import random
import requests

from .moves import Move

class Pokemon(object):
    moves_dict = {}

    def __init__(self, url, pokemon_info=None):
        self.pokemon_info = pokemon_info or self.get_from_api(url)

        self._name = None
        self._hp = None
        self._moves_list = []

    @property
    def hp(self):
        if self.pokemon_info is None:
            self.pokemon_info = self.get_from_api()

        stats = self.pokemon_info['stats']
        h = [i['base_stat'] for i in stats if i['stat']['name'] == 'hp']
        self._hp = h[0]

        return self._hp

    @property
    def name(self):
        if self.pokemon_info is None:
            self.pokemon_info = self.get_from_api()

        self._name = self.pokemon_info['name']

        return self._name

    @property
    def moves(self):
        if self.pokemon_info is None:
            self.pokemon_info = self.get_from_api()

        self._moves_list = self.pokemon_info['moves']

        return self._moves_list

    def get_from_api(self, url):
        """ Retrieves pokemon info from web API """
        logging.info("Retrieving pokemon from api url: {}".format(url))
        res = requests.get(url)
        res.raise_for_status()
        info = res.json()

        return info

    def random_move(self):
        """ Chooses a random move from moves_list

        Memoizes moves in moves_dict for faster retrieval later

        """
        rand_int = random.randint(0, len(self.moves) - 1)
        move = self.moves[rand_int]

        move_name = move['move']['name']
        if move_name not in self.moves_dict:
            self.moves_dict[move_name] = Move(move['move']['url'])

        return self.moves_dict[move_name]

