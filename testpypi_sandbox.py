"""Simple sandbox module to upload to TestPyPI."""

__version__ = "0.0.3"


def main() -> None:
    print_message()


def print_message() -> None:
    message = get_message()
    print(message)


def get_message() -> str:
    return "Welcome to TestPyPI-sandbox!"


if __name__ == "__main__":
    main()
