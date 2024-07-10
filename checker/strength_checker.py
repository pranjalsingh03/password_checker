import re
from .base_strategy import PasswordStrategy

class PasswordStrengthChecker(PasswordStrategy):
    def evaluate(self, password: str) -> str:
        if len(password) < 8:
            return "Weak"
        if not re.search("[a-z]", password):
            return "Weak"
        if not re.search("[A-Z]", password):
            return "Moderate"
        if not re.search("[0-9]", password):
            return "Moderate"
        if not re.search("[@#$%^&*!]", password):
            return "Strong"
        return "Very Strong"
