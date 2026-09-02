import secrets
import string

from .base import PasswordGenerator


class PinGenerator(PasswordGenerator):
    """Generate numeric PINs."""

    def __init__(self, length: int = 6):
        if length < 1:
            raise ValueError("PIN length must be at least 1.")

        self.length = length

    def generate(self) -> str:
        """Generate a numeric PIN."""

        return "".join(
            secrets.choice(string.digits)
            for _ in range(self.length)
        )