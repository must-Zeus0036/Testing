# test_player.py
import unittest
from player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        """Set up a Player instance for testing."""
        self.player = Player("Adam")

    def test_initial_state(self):
        """Test that the player's initial state is set up correctly."""
        self.assertEqual(self.player.name, "Adam", "Player name should be 'Adam'")
        self.assertEqual(self.player.total_score, 0, "Initial total score should be 0")
        self.assertEqual(self.player.turn_score, 0, "Initial turn score should be 0")

    def test_add_turn_score(self):
        """Test adding to the player's turn score."""
        self.player.add_turn_score(10)
        self.assertEqual(self.player.turn_score, 10, "Turn score should be 10 after adding 10")

        self.player.add_turn_score(5)
        self.assertEqual(self.player.turn_score, 15, "Turn score should be 15 after adding 5")

    def test_reset_turn_score(self):
        """Test resetting the player's turn score."""
        self.player.add_turn_score(10)
        self.player.reset_turn_score()
        self.assertEqual(self.player.turn_score, 0, "Turn score should be reset to 0")

    def test_add_total_score(self):
        """Test adding the turn score to the total score."""
        self.player.add_turn_score(10)
        self.player.add_total_score()
        self.assertEqual(self.player.total_score, 10, "Total score should be 10 after adding turn score")
        self.assertEqual(self.player.turn_score, 0, "Turn score should be reset to 0 after adding to total score")

    def test_get_total_score(self):
        """Test retrieving the player's total score."""
        self.player.add_turn_score(10)
        self.player.add_total_score()
        self.assertEqual(self.player.get_total_score(), 10, "get_total_score() should return 10")

if __name__ == "__main__":
    unittest.main()
