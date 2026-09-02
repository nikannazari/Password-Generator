import secrets
from pathlib import Path
import nltk

from .base import PasswordGenerator


DEFAULT_WORDS = [
    "apple",
    "bridge",
    "castle",
    "cloud",
    "coffee",
    "forest",
    "garden",
    "guitar",
    "island",
    "jungle",
    "keyboard",
    "lemon",
    "mountain",
    "ocean",
    "orange",
    "planet",
    "python",
    "river",
    "rocket",
    "shadow",
    "silver",
    "summer",
    "thunder",
    "tiger",
    "window",
]

nltk.download('words')


class MemorablePasswordGenerator(PasswordGenerator):
    """Generate memorable passwords using random words."""

    def __init__(
        self,
        easy,
        num_of_words: int = 4,
        separator: str = "-",
        capitalization: bool = False,
        vocabulary: list[str] | None = None,
    ):
        if num_of_words < 1:
            raise ValueError(
                "Number of words must be at least 1."
            )

        self.num_of_words = num_of_words
        self.separator = separator
        self.capitalization = capitalization
        self.easy = easy
        self.vocabulary = (nltk.corpus.words.words() if easy == True else DEFAULT_WORDS)

        if not self.vocabulary:
            raise ValueError("Vocabulary cannot be empty.")

    def generate(self) -> str:
        """Generate a memorable password."""

        words = [
            secrets.choice(self.vocabulary)
            for _ in range(self.num_of_words)
        ]

        if self.capitalization:
            words = [
                word.capitalize()
                for word in words
            ]

        return self.separator.join(words)