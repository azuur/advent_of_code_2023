from functools import reduce
import operator
import re

from inputs.get_input import get_inp

test_case_1, test_case_2, inp = get_inp(__file__)


def calculate_calibration(line: str) -> int:
    digits = [d for d in line if d.isdigit()]
    return int(digits[0] + digits[-1])


def solve_1(inp: list[str]) -> int:
    calibrations = map(calculate_calibration, inp)
    return reduce(operator.add, calibrations)


def replace_spelled_digits(line: str) -> str:
    spelled_digits = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    spelled_digits = dict(zip(spelled_digits, range(1, 10)))

    def rep(match: re.Match) -> str:
        return str(spelled_digits[match.group()])

    reg = f"({'|'.join(spelled_digits.keys())})"

    aft = line
    while True:
        bef = aft
        aft = re.sub(reg, rep, aft)
        if bef == aft:
            return aft


def solve_2(inp: list[str]) -> int:
    inp = map(replace_spelled_digits, inp)
    calibrations = map(calculate_calibration, inp)
    return reduce(operator.add, calibrations)


if __name__ == "__main__":
    print(solve_1(test_case_1))
    print(solve_1(inp))

    print(solve_2(test_case_2))
    print(solve_2(inp))
