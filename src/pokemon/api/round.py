import logging

class Round(object):
    """ A Round consists of the hp pools, the move, and damage amount """
    def __init__(self, hp_1, hp_2, round_number):
        self.player_1 = {
            "move_name": None,
            "move_dmg": 0,
            "hp": hp_1
        }
        self.player_2 = {
            "move_name": None,
            "move_dmg": 0,
            "hp": hp_2
        }

        self.round_number = round_number

    def to_dict(self):
        """ Serializes the class to a dictionary """
        round_info = {
            'round': self.round_number,
            'player_1': self.player_1,
            'player_2': self.player_2
        }

        return round_info

    def fight(self, player_1_action, player_2_action):
        """ Given move objects, subract the move_power from the opponnents hp

        """
        self.player_1.update(player_1_action)
        self.player_2.update(player_2_action)

        logging.info('move 1: {}'.format(player_1_action['move_name']))
        logging.info('move 2: {}'.format(player_2_action['move_name']))

        # If/elif/else prevents a player who has been knocked out from
        # performing his action
        if self.player_2['hp'] - player_1_action['move_dmg'] < 0:
            self.player_2['hp'] -= player_1_action['move_dmg']

        elif self.player_1['hp'] - player_2_action['move_dmg'] < 0:
            self.player_1['hp'] -= player_2_action['move_dmg']

        else:
            self.player_2['hp'] -= player_1_action['move_dmg']
            self.player_1['hp'] -= player_2_action['move_dmg']

        return self.player_1['hp'], self.player_2['hp']
