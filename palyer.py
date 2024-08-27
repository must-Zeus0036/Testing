
class Player:
    """Class representing a player in the game."""

    def __init__(self, name):
        self.name = name
        self.total_score = 0
        self.turn_score = 0

    def reset_turn_score(self):
        """Reset the turn score to zero."""
        self.turn_score = 0
