from generators import (
    MemorablePasswordGenerator,
    PinGenerator,
    RandomPasswordGenerator,
)
from utils.validators import parse_bool, validate_length


def display_header() -> None:
    """Display the application header."""

    print("=" * 50)
    print("             PASSWORD GENERATOR")
    print("=" * 50)


def display_menu() -> None:
    """Display the generator menu."""

    print()
    print("[1] PIN")
    print("[2] Random Password")
    print("[3] Memorable Password")
    print("[Q] Quit")
    print()


def generate_pin() -> str:
    """Generate a PIN from user input."""

    length = int(input("PIN length >>> "))
    length = validate_length(length, 1, 32)

    generator = PinGenerator(length)

    return generator.generate()


def generate_random_password() -> str:
    """Generate a random password from user input."""

    length = int(input("Password length >>> "))
    length = validate_length(length, 1, 128)

    include_numbers = parse_bool(
        input("Include numbers? [true/false] >>> ")
    )

    include_symbols = parse_bool(
        input("Include symbols? [true/false] >>> ")
    )

    generator = RandomPasswordGenerator(
        length=length,
        include_numbers=include_numbers,
        include_symbols=include_symbols,
    )

    return generator.generate()


def generate_memorable_password() -> str:
    """Generate a memorable password from user input."""

    number_of_words = int(
        input("Number of words >>> ")
    )

    number_of_words = validate_length(
        number_of_words,
        2,
        12,
    )

    separator = input(
        "Separator [default: -] >>> "
    )

    if not separator:
        separator = "-"

    capitalization = parse_bool(
        input(
            "Capitalize words? [true/false] >>> "
        )
    )

    generator = MemorablePasswordGenerator(
        num_of_words=number_of_words,
        separator=separator,
        capitalization=capitalization,
        easy=True
    )

    return generator.generate()


def main() -> None:
    """Run the password generator CLI."""

    display_header()

    while True:
        display_menu()

        choice = input("Choose an option >>> ").strip().lower()

        if choice in {"q", "quit", "exit"}:
            print("\nGoodbye! 👋")
            break

        try:
            if choice == "1":
                password = generate_pin()

            elif choice == "2":
                password = generate_random_password()

            elif choice == "3":
                password = generate_memorable_password()

            else:
                print("Invalid option. Please try again.")
                continue

            print()
            print("=" * 50)
            print(f"Generated Password: {password}")
            print("=" * 50)

        except ValueError as error:
            print(f"\nError: {error}")


if __name__ == "__main__":
    main()