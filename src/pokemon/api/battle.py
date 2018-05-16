import random

from .round import Round

class Battle(object):
    def __init__(self, pokemon_1_info, pokemon_2_info):
        self.pokemon_1_info = pokemon_1_info
        self.pokemon_2_info = pokemon_2_info

    @classmethod
    def get_hp(cls, stats):
        hp = [i['base_stat'] for i in stats if i['stat']['name'] == 'hp']

        return hp[0]

    def choose_random_move(self, moves_list):
        rand_int = random.randint(0, len(moves_list) - 1)
        move = moves_list[rand_int]

        return move

    def execute(self):
        hp_1 = self.get_hp(self.pokemon_1_info['stats'])
        hp_2 = self.get_hp(self.pokemon_2_info['stats'])

        moves_list_1 = self.pokemon_1_info['moves']
        moves_list_2 = self.pokemon_2_info['moves']

        initial_round = Round(hp_1, hp_2, 0)
        battle = [initial_round.to_dict()]

        battle_round_number = 1
        while (hp_1 > 0) and (hp_2 > 0):
            battle_round = Round(hp_1, hp_2, battle_round_number)

            player_1_move = self.choose_random_move(moves_list_1)
            player_2_move = self.choose_random_move(moves_list_2)

            battle_round.fight(player_1_move, player_2_move)

            battle.append(battle_round.to_dict())

            battle_round_number += 1
            hp_1 = battle_round.player_1_hp
            hp_2 = battle_round.player_2_hp

        if hp_2 <= 0:
            winner = "Player 1: {}".format(self.pokemon_1_info['name'])
        elif hp_1 <= 0:
            winner = "Player 2: {}".format(self.pokemon_2_info['name'])

        return battle, winner

