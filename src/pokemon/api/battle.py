
from .round import Round

class Battle(object):
    """ A Battle consists of two pokemon, a list of rounds, and a winner """
    def __init__(self, pokemon_1, pokemon_2):
        self.rounds = []
        self.winner = None
        self.round_number = 0
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2

    def battle_random_attacks(self, power_percent):
        """ Executes a battle with a scaling factor to each attack

        Attacks are chosen randomly from a pokemon's move list

        Battle ends when one pokemon's hp is less than zero

        """
        hp_1 = self.pokemon_1.hp
        hp_2 = self.pokemon_2.hp

        initial_round = Round(hp_1, hp_2, self.round_number)
        self.rounds.append(initial_round.to_dict())

        while (hp_1 > 0) and (hp_2 > 0):
            self.round_number += 1
            battle_round = Round(hp_1, hp_2, self.round_number)

            player_1_move = self.pokemon_1.random_move()
            player_2_move = self.pokemon_2.random_move()

            battle_round.fight(player_1_move, player_2_move, power_percent)

            self.rounds.append(battle_round.to_dict())

            hp_1 = battle_round.player_1_hp
            hp_2 = battle_round.player_2_hp

        if hp_2 <= 0:
            self.winner = "Player 1: {}".format(self.pokemon_1.name)
        elif hp_1 <= 0:
            self.winner = "Player 2: {}".format(self.pokemon_2.name)


