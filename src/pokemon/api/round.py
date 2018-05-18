import logging

from .moves import Move

class Round(object):
    """ A Round consists of the hp pools, the move, and damage amount """
    def __init__(self, hp_1, hp_2, round_number):
        self.player_1_hp = hp_1
        self.player_2_hp = hp_2

        self.player_1_move = Move(None)
        self.player_2_move = Move(None)

        self.player_1_attack = 0
        self.player_2_attack = 0

        self.round_number = round_number

    def to_dict(self):
        """ Serializes the class to a dictionary """
        round_info = {
            'round': self.round_number,
            'player_1_move': self.player_1_move.name,
            'player_1_power': self.player_1_attack,
            'player_1_hp': self.player_1_hp,
            'player_2_move': self.player_2_move.name,
            'player_2_power': self.player_2_attack,
            'player_2_hp': self.player_2_hp
        }

        return round_info

    def fight(self, player_1_move, player_2_move, power_percent):
        """ Given move objects, subract the move_power from the opponnents hp

        """
        self.player_1_move = player_1_move
        self.player_2_move = player_2_move

        logging.info('move 1: {}'.format(self.player_1_move.name))
        logging.info('move 2: {}'.format(self.player_2_move.name))

        self.player_1_attack = self.player_1_move.power * power_percent
        self.player_2_attack = self.player_2_move.power * power_percent

        if self.player_2_hp - self.player_1_attack < 0:
            self.player_2_hp -= self.player_1_attack

        elif self.player_1_hp - self.player_2_attack < 0:
            self.player_1_hp -= self.player_2_attack

        else:
            self.player_2_hp -= self.player_1_attack
            self.player_1_hp -= self.player_2_attack
