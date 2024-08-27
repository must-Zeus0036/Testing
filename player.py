
class Player:
    """Class representing a player in the game."""

    def __init__(self, name):
        self.name = name
        self.total_score = 0
        self.turn_score = 0

    def reset_turn_score(self):
        """Reset the turn score to zero."""
        self.turn_score = 0

    def add_turn_score(self, score):
        """Add the score to the player's turn score."""
        self.turn_score += score

    def add_total_score(self):
        """Add the turn score to the total score and reset turn score."""
        self.total_score += self.turn_score
        self.reset_turn_score()

    def get_total_score(self):
        """Return the player's total score."""
        return self.total_score

if __name__ == "__main__":
    player = Player("Adam")
    player.add_turn_score(10)
    player.add_total_score()
    print(f"{player.name}'s total score is {player.get_total_score()}")
