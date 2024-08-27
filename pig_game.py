import sys
import io

# Set UTF-8 encoding for standard output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from die import Die
from player import Player

class PigGame:
    """Class representing the Pig Dice Game."""

    def __init__(self, player_names, winning_score=100):
        self.players = [Player(name) for name in player_names]
        self.die = Die()
        self.winning_score = winning_score
        self.current_player_index = 0

    def switch_turn(self):
        """Switch the turn to the next player."""
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def current_player(self):
        """Return the current player."""
        return self.players[self.current_player_index]

    def play_turn(self):
        """Play a single turn for the current player."""
        player = self.current_player()
        print(f"\n{player.name}'s turn. Total score: {player.get_total_score()}")

        while True:
            choice = input("Enter 'r' to roll or 'h' to hold: ").strip().lower()
            if choice == 'r':
                roll = self.die.roll()
                print(f"{player.name} rolled: {roll}")
                for line in self.die.display(roll):
                    print(line)

                if roll == 1:
                    print(f"{player.name} rolled a 1! Turn over, no points added.")
                    player.reset_turn_score()
                    self.switch_turn()
                    break
                else:
                    player.add_turn_score(roll)
                    print(f"Turn score: {player.turn_score}")
            elif choice == 'h':
                player.add_total_score()
                print(f"{player.name} holds. Total score: {player.get_total_score()}")
                self.switch_turn()
                break
            else:
                print("Invalid input. Please enter 'r' to roll or 'h' to hold.")

    def play_game(self):
        """Play the entire game until a player wins."""
        while True:
            self.play_turn()
            for player in self.players:
                if player.get_total_score() >= self.winning_score:
                    print(f"\n{player.name} wins with {player.get_total_score()} points!")
                    return

if __name__ == "__main__":
    player_names = input("Enter player names, separated by commas: ").split(",")
    player_names = [name.strip() for name in player_names]

    game = PigGame(player_names)
    game.play_game()
