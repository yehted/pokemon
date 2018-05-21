import mock
import unittest

import pokemon.api.round as mod_ut

class TestRound(unittest.TestCase):
    def test_fight(self):
        """ Round where both players take non-lethal damage """
        test_round = mod_ut.Round(10, 9, 1)

        player_1_action = {
                'move_name': 'hit',
                'move_dmg': 3
            }
        player_2_action = {
                'move_name': 'slam',
                'move_dmg': 4
            }

        hp_1, hp_2 = test_round.fight(player_1_action, player_2_action)

        self.assertEqual(hp_1, 6)
        self.assertEqual(hp_2, 6)

    def test_fight_p1_wins(self):
        """ Round where player2 takes fatal damage before being able to deal
        damage to player1

        """
        test_round = mod_ut.Round(10, 2, 1)

        player_1_action = {
                'move_name': 'hit',
                'move_dmg': 3
            }
        player_2_action = {
                'move_name': 'slam',
                'move_dmg': 4
            }

        hp_1, hp_2 = test_round.fight(player_1_action, player_2_action)

        self.assertEqual(hp_1, 10)
        self.assertEqual(hp_2, -1)

    def test_fight_p2_wins(self):
        """ Round where player1 takes fatal damage after dealing
        damage to player2

        """
        test_round = mod_ut.Round(2, 10, 1)

        player_1_action = {
                'move_name': 'hit',
                'move_dmg': 3
            }
        player_2_action = {
                'move_name': 'slam',
                'move_dmg': 4
            }

        hp_1, hp_2 = test_round.fight(player_1_action, player_2_action)

        self.assertEqual(hp_1, -2)
        self.assertEqual(hp_2, 7)

if __name__ == '__main__':
    unittest.main()
