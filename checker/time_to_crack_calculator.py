import math
from .base_strategy import PasswordStrategy

class TimeToCrackCalculator(PasswordStrategy):
    def evaluate(self, password: str) -> str:
        char_set_size = 0
        if any(c.islower() for c in password):
            char_set_size += 26
        if any(c.isupper() for c in password):
            char_set_size += 26
        if any(c.isdigit() for c in password):
            char_set_size += 10
        if any(c in '@#$%^&*!' for c in password):
            char_set_size += 8
        
        combinations = char_set_size ** len(password)
        seconds_to_crack = combinations / 1e6  # Assume 1 million attempts per second

        if seconds_to_crack < 60:
            return "less than a minute"
        elif seconds_to_crack < 3600:
            return f"{seconds_to_crack / 60:.2f} minutes"
        elif seconds_to_crack < 86400:
            return f"{seconds_to_crack / 3600:.2f} hours"
        else:
            return f"{seconds_to_crack / 86400:.2f} days"
