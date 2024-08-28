import unittest
from die import Die

class TestDie(unittest.TestCase):

    def setUp(self):
        self.die = Die()

    def test_roll_range(self):
        for _ in range(100):  # Roll the die multiple times
            result = self.die.roll()
            self.assertIn(result, range(1, 7))

    def test_display(self):
        for value in range(1, 7):
            art = self.die.display(value)
            self.assertEqual(len(art), 5)  # Check if ASCII art has 5 lines
            self.assertTrue(all(line.startswith("└") or line.startswith("┐") or "●" in line for line in art))

if __name__ == "__main__":
    unittest.main()
