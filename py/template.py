from inputs.get_input import get_inp

test_case_1, test_case_2, inp = get_inp(__file__)


def solve_1(inp: list[str]):
    pass


def solve_2(inp: list[str]):
    pass


if __name__ == "__main__":
    print(solve_1(test_case_1))
    print(solve_1(inp))

    print(solve_2(test_case_2))
    print(solve_2(inp))
