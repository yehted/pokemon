import logging

from .moves import Moves

class Round(object):
    def __init__(self, hp_1, hp_2, round_number):
        self.player_1_hp = hp_1
        self.player_2_hp = hp_2

        self.move_1_name = None
        self.move_2_name = None

        self.move_1_power = 0
        self.move_2_power = 0

        self.round_number = round_number

    def to_dict(self):
        round_info = {
            'round': self.round_number,
            'player_1_move': self.move_1_name,
            'player_1_power': self.move_1_power,
            'player_1_hp': self.player_1_hp,
            'player_2_move': self.move_2_name,
            'player_2_power': self.move_2_power,
            'player_2_hp': self.player_2_hp
        }

        return round_info

    def fight(self, player_1_move, player_2_move):
        self.move_1_name = player_1_move['move']['name']
        self.move_2_name = player_2_move['move']['name']
        logging.info('move 1: {}'.format(self.move_1_name))
        logging.info('move 2: {}'.format(self.move_2_name))

        move_1_url = player_1_move['move']['url']
        move_2_url = player_2_move['move']['url']

        self.move_1_power = Moves.get_move_power(move_1_url)
        self.move_2_power = Moves.get_move_power(move_2_url)

        if self.player_2_hp - self.move_1_power < 0:
            self.player_2_hp -= self.move_1_power

        elif self.player_1_hp - self.move_2_power < 0:
            self.player_1_hp -= self.move_2_power

        else:
            self.player_2_hp -= self.move_1_power
            self.player_1_hp -= self.move_2_power

        return
