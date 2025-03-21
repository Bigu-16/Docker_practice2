import io
import sys
from main import fizzBuzz

def test_fizzBuzz():
    test_cases = [
        (15, "FizzBuzz"),
        (3, "Fizz"),
        (5, "Buzz"),
        (7, "7")
    ]

    for num, expected in test_cases:

        result = fizzBuzz(num)

        assert result == expected, f"Expected {expected}, but got {result}"

if __name__ == "__main__":
    test_fizzBuzz()