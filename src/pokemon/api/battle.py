
from .round import Round

class Battle(object):
    """ A Battle consists of two pokemon """
    def __init__(self, pokemon_1, pokemon_2):
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2

    def go(self):
        """ Returns a list of rounds and a winner """
        pass

class RandomBattle(Battle):
    def go(self, power_percent):
        """ Executes a battle with a scaling factor to each attack

        Attacks are chosen randomly from a pokemon's move list

        Battle ends when one pokemon's hp is less than zero

        """
        rounds = []
        round_number = 0

        hp_1 = self.pokemon_1.hp
        hp_2 = self.pokemon_2.hp

        initial_round = Round(hp_1, hp_2, round_number)
        rounds.append(initial_round.to_dict())

        while (hp_1 > 0) and (hp_2 > 0):
            round_number += 1
            battle_round = Round(hp_1, hp_2, round_number)

            player_1_move = self.pokemon_1.random_move()
            player_2_move = self.pokemon_2.random_move()

            player_1_action = {
                "move_name": player_1_move.name,
                "move_dmg": player_1_move.power * power_percent,
            }

            player_2_action = {
                "move_name": player_2_move.name,
                "move_dmg": player_2_move.power * power_percent,
            }

            hp_1, hp_2 = battle_round.fight(player_1_action, player_2_action)

            rounds.append(battle_round.to_dict())


        if hp_2 <= 0:
            winner = "Player 1: {}".format(self.pokemon_1.name)
        elif hp_1 <= 0:
            winner = "Player 2: {}".format(self.pokemon_2.name)

        return rounds, winner


