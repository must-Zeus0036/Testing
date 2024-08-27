import random

class Die:
    """Class representing a dice with ASCII"""
    
    DICE_ART = {
        1: (
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
    }

    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        """Simulate rolling the die and return a random face value."""
        return random.randint(1, self.sides)

    def display(self, value):
        """Return the ASCII art representation of the die face value."""
        return self.DICE_ART[value]

if __name__ == "__main__":
    die = Die()
    roll_result = die.roll()
    print(f"Rolled a {roll_result}!")
    for line in die.display(roll_result):
        print(line)
        
