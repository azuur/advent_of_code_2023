from collections import defaultdict
from functools import reduce
import operator
import re

from inputs.get_input import get_inp

test_case_1, test_case_2, inp = get_inp(__file__)


def get_symbols(lines: list[str]):
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if not c.isdigit() and not c == ".":
                yield c, (i, j)


def get_numbers(lines: list[str]):
    for i, line in enumerate(lines):
        matches = re.finditer(r"\d+", line)
        for m in matches:
            yield int(m.group()), (i, m.span())


def adjacent(n_c: tuple[int, tuple[int, int]], s_c: [int, int]):
    row_condition = abs(n_c[0] - s_c[0]) < 2
    column_condition = (n_c[1][0] - 1 - s_c[1]) * (n_c[1][1] - s_c[1]) <= 0
    return bool(row_condition and column_condition)


def get_adjacent_lines(lines: list[str], row_num: int):
    return lines[max(row_num - 1, 0) : row_num + 2]


def get_symbols_in_adjacent_lines(lines: list[str], row_num: int):
    adj_lines = get_adjacent_lines(lines, row_num)
    for s, (i, j) in get_symbols(adj_lines):
        yield s, (i + max(row_num - 1, 0), j)


def get_numbers_in_adjacent_lines(lines: list[str], row_num: int):
    adj_lines = get_adjacent_lines(lines, row_num)
    for num, (i, span) in get_numbers(adj_lines):
        yield num, (i + max(row_num - 1, 0), span)


def get_adjacencies(inp: list[str]):
    number_adjacencies = defaultdict(list)
    symbol_adjacencies = defaultdict(list)
    for n, n_coords in get_numbers(inp):
        for s, s_coords in get_symbols_in_adjacent_lines(inp, n_coords[0]):
            if adjacent(n_coords, s_coords):
                number_adjacencies[(n, n_coords)].append((s, s_coords))
                symbol_adjacencies[(s, s_coords)].append((n, n_coords))
    return number_adjacencies, symbol_adjacencies


def get_part_numbers(inp: list[str]):
    number_adjacencies, _ = get_adjacencies(inp)
    return [k[0] for k in number_adjacencies.keys()]


def symbols_nearby(lines: list[str], n_coords: tuple[int, tuple[int, int]]):
    lines = get_adjacent_lines(lines, n_coords[0])
    l, u = n_coords[1]
    l, u = max(l - 1, 0), u + 1
    section = [line[l:u] for line in lines]
    print("\n" + "\n".join(section) + "\n")
    return not all(c.isdigit() or c == "." for row in section for c in row)


def get_part_numbers_alt(inp: list[str]):
    for n, n_coords in get_numbers(inp):
        if symbols_nearby(inp, n_coords):
            yield n


def get_gears(inp: list[str]):
    number_adjacencies, symbol_adjacencies = get_adjacencies(inp)
    part_numbers = set(number_adjacencies.keys())
    gears = {
        part: part_numbers.intersection(numbers)
        for part, numbers in symbol_adjacencies.items()
    }
    gears = {
        part: part_numbers
        for part, part_numbers in symbol_adjacencies.items()
        if part[0] == "*" and len(part_numbers) == 2
    }
    return gears


def solve_1(inp: list[str]):
    return sum(get_part_numbers(inp))


def solve_2(inp: list[str]):
    gear_part_numbers = [
        [num[0] for num in nums] for nums in get_gears(inp).values()
    ]
    return sum(map(lambda nums: reduce(operator.mul, nums), gear_part_numbers))


if __name__ == "__main__":
    print(solve_1(test_case_1))
    print(solve_1(inp))

    print(solve_2(test_case_2))
    print(solve_2(inp))
