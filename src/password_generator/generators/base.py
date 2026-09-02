from abc import ABC, abstractmethod


class PasswordGenerator(ABC):
    """Abstract base class for password generators."""

    @abstractmethod
    def generate(self) -> str:
        """Generate and return a password."""
        raise NotImplementedError