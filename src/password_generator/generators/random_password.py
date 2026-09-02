import secrets
import string

from .base import PasswordGenerator


class RandomPasswordGenerator(PasswordGenerator):
    """Generate random passwords."""

    def __init__(
        self,
        length: int = 12,
        include_numbers: bool = True,
        include_symbols: bool = True,
    ):
        if length < 1:
            raise ValueError("Password length must be at least 1.")

        self.length = length
        self.include_numbers = include_numbers
        self.include_symbols = include_symbols

        self.characters = string.ascii_letters

        if self.include_numbers:
            self.characters += string.digits

        if self.include_symbols:
            self.characters += string.punctuation

    def generate(self) -> str:
        """Generate a random password."""

        return "".join(
            secrets.choice(self.characters)
            for _ in range(self.length)
        )