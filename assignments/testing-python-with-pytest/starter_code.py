"""Functions to test in the Testing Python Programs with pytest assignment."""


def calculate_average(numbers: list[float]) -> float:
    """Return the average of a non-empty list of numbers."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def is_valid_password(password: str) -> bool:
    """Return whether a password has at least eight characters."""
    return len(password) >= 8


def find_max(numbers: list[int]) -> int:
    """Return the largest number in a non-empty list."""
    if not numbers:
        raise ValueError("numbers must not be empty")
    return max(numbers)
