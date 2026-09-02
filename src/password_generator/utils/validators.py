def validate_length(
    length: int,
    minimum: int = 1,
    maximum: int = 128,
) -> int:
    """Validate a password length."""

    if not minimum <= length <= maximum:
        raise ValueError(
            f"Length must be between {minimum} and {maximum}."
        )

    return length


def parse_bool(value: str) -> bool:
    """Convert common textual boolean values to bool."""

    normalized = value.strip().lower()

    if normalized in {"true", "yes", "y", "1"}:
        return True

    if normalized in {"false", "no", "n", "0"}:
        return False

    raise ValueError(
        "Please enter true/false, yes/no, y/n, or 1/0."
    )