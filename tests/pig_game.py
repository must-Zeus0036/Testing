import unittest
from unittest.mock import patch, MagicMock
from pig_game import PigGame
from player import Player
from die import Die

class TestPigGame(unittest.TestCase):

    def setUp(self):
        """Set up the game with two players for testing."""
        self.game = PigGame(["Alice", "Bob"], winning_score=20)
    
    def test_initialization(self):
        """Test that the game is initialized with the correct players and winning score."""
        self.assertEqual(len(self.game.players), 2, "Game should have 2 players.")
        self.assertEqual(self.game.players[0].name, "Alice", "First player should be Alice.")
        self.assertEqual(self.game.players[1].name, "Bob", "Second player should be Bob.")
        self.assertEqual(self.game.winning_score, 20, "Winning score should be 20.")

    @patch('builtins.input', side_effect=['r', 'h'])
    def test_play_turn_roll_and_hold(self, mock_input):
        """Test a turn where the player rolls and then holds."""
        # Mock the die roll to return a 5
        self.game.die.roll = MagicMock(return_value=5)

        # Run the player's turn
        self.game.play_turn()

        # Check that the player's turn score is updated
        self.assertEqual(self.game.players[0].turn_score, 0, "Turn score should reset after holding.")
        self.assertEqual(self.game.players[0].total_score, 5, "Total score should be updated after holding.")
        self.assertEqual(self.game.current_player_index, 1, "Turn should switch to the next player.")

    @patch('builtins.input', side_effect=['r', 'r', 'h'])
    def test_play_turn_roll_twice_and_hold(self, mock_input):
        """Test a turn where the player rolls twice and then holds."""
        # Mock the die rolls to return 3 and 4
        self.game.die.roll = MagicMock(side_effect=[3, 4])

        # Run the player's turn
        self.game.play_turn()

        # Check that the player's turn score is updated correctly
        self.assertEqual(self.game.players[0].turn_score, 0, "Turn score should reset after holding.")
        self.assertEqual(self.game.players[0].total_score, 7, "Total score should be updated correctly after holding.")
        self.assertEqual(self.game.current_player_index, 1, "Turn should switch to the next player.")

    @patch('builtins.input', side_effect=['r'])
    def test_play_turn_roll_one(self, mock_input):
        """Test a turn where the player rolls a 1."""
        # Mock the die roll to return a 1
        self.game.die.roll = MagicMock(return_value=1)

        # Run the player's turn
        self.game.play_turn()

        # Check that the player's turn score is reset and no points are added to the total score
        self.assertEqual(self.game.players[0].turn_score, 0, "Turn score should be reset to 0 after rolling a 1.")
        self.assertEqual(self.game.players[0].total_score, 0, "Total score should remain 0 after rolling a 1.")
        self.assertEqual(self.game.current_player_index, 1, "Turn should switch to the next player.")

    @patch('builtins.input', side_effect=['r', 'h', 'r', 'r', 'h', 'r', 'h'])
    def test_play_game_winning_condition(self, mock_input):
        """Test that the game ends when a player reaches the winning score."""
        # Mock die rolls to ensure a player reaches the winning score
        self.game.die.roll = MagicMock(side_effect=[5, 5, 5, 5])

        with patch('builtins.print') as mock_print:  # Mock print to capture output
            self.game.play_game() #pragma: no cover

            # Check that the game ends with the correct winner
            self.assertIn("Alice wins with 20 points!", [args[0] for args in mock_print.call_args_list])

if __name__ == "__main__":
    unittest.main()
