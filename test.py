import io
import sys
from main import fizzBuzz

def test_fizzBuzz():
    output = io.StringIO()
    sys.stdout = output

    fizzBuzz(15)

    sys.stdout = sys.__stdout__
    result = output.getvalue().strip()
    expected = "FizzBuzz"
    assert result == expected, f"Expected {expected}, but got {result}"

if __name__ == "__main__":
    test_fizzBuzz()
    print("All tests passed!")