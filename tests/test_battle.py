import mock
import unittest

import pokemon.api.battle as mod_ut

class TestRandomBattle(unittest.TestCase):
    def test_go(self):
        # Set up pokemon
        mock_pokemon_1 = mock.Mock(hp=10)
        mock_pokemon_2 = mock.Mock(hp=10)
        mock_pokemon_1.name = 'name_1'
        mock_pokemon_2.name = 'name_2'

        # Set up moves
        mock_move_1 = mock.Mock(power=4)
        mock_move_2 = mock.Mock(power=3)
        mock_move_1.name = 'hit'
        mock_move_2.name = 'slam'

        # Both pokemon use the same move every time (for simplicity)
        mock_pokemon_1.random_move.return_value = mock_move_1
        mock_pokemon_2.random_move.return_value = mock_move_2

        test_battle = mod_ut.RandomBattle(mock_pokemon_1, mock_pokemon_2)

        rounds, winner = test_battle.go(power_percent=1.0)

        expected_rounds = [
                {
                    'round': 0,
                    'player_1': {
                        'move_name': None,
                        'move_dmg': 0,
                        'hp': 10
                    },
                    'player_2': {
                        'move_name': None,
                        'move_dmg': 0,
                        'hp': 10
                    }
                },
                {
                    'round': 1,
                    'player_1': {
                        'move_name': 'hit',
                        'move_dmg': 4,
                        'hp': 7
                    },
                    'player_2': {
                        'move_name': 'slam',
                        'move_dmg': 3,
                        'hp': 6
                    }
                },
                {
                    'round': 2,
                    'player_1': {
                        'move_name': 'hit',
                        'move_dmg': 4,
                        'hp': 4
                    },
                    'player_2': {
                        'move_name': 'slam',
                        'move_dmg': 3,
                        'hp': 2
                    }
                },
                {
                    'round': 3,
                    'player_1': {
                        'move_name': 'hit',
                        'move_dmg': 4,
                        'hp': 4
                    },
                    'player_2': {
                        'move_name': 'slam',
                        'move_dmg': 3,
                        'hp': -2
                    }
                }
            ]

        expected_winner = "Player 1: name_1"

        self.assertEqual(winner, expected_winner)
        self.assertEqual(rounds, expected_rounds)

if __name__ == '__main__':
    unittest.main()
