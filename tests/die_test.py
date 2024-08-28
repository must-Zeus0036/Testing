# test_die.py
import unittest
from die import Die

class TestDie(unittest.TestCase):

    def setUp(self):
        """Set up a Die instance for testing."""
        self.die = Die()

    def test_roll(self):
        """Test that rolling the die returns a value between 1 and 6."""
        roll_result = self.die.roll()
        self.assertIn(roll_result, range(1, 7), "Roll result should be between 1 and 6")

    def test_display(self):
        """Test that the display method returns the correct ASCII art."""
        # Test display for each value from 1 to 6
        for value in range(1, 7):
            art = self.die.display(value)
            self.assertEqual(art, self.die.DICE_ART[value], f"Display for {value} is incorrect")

    def test_invalid_display(self):
        """Test that display method raises an error for invalid values."""
        with self.assertRaises(KeyError):
            self.die.display(0)  # 0 is not a valid die face

        with self.assertRaises(KeyError):
            self.die.display(7)  # 7 is not a valid die face


if __name__ == "__main__":
    unittest.main()
