from collections import defaultdict
from functools import reduce
import operator
from dataclasses import dataclass

from inputs.get_input import get_inp

test_case_1, test_case_2, inp = get_inp(__file__)


@dataclass
class CubeCount:
    color: str
    num: int


@dataclass
class Draw:
    cube_counts: list[CubeCount]


@dataclass
class Game:
    gid: int
    draws: list[Draw]


def parse_draw(draw: str):
    cube_counts = map(str.strip, draw.split(","))
    cube_counts = [c.split() for c in cube_counts]
    cube_counts = [CubeCount(color=c[1], num=int(c[0])) for c in cube_counts]
    return Draw(cube_counts=cube_counts)


def parse_game(line: str):
    l, r = line.split(":")
    game_id = int(l.split()[-1])
    draws = map(str.strip, r.strip().split(";"))
    draws = list(map(parse_draw, draws))
    return Game(gid=game_id, draws=draws)


def possible(game: Game, bag: dict[str, int]):
    return all(
        c.num <= bag[c.color] for d in game.draws for c in d.cube_counts
    )


def min_cubes(game: Game):
    result = defaultdict(lambda: 0)
    for d in game.draws:
        for c in d.cube_counts:
            result[c.color] = max(result[c.color], c.num)
    return result


def solve_1(inp: list[str]):
    bag = {"red": 12, "green": 13, "blue": 14}
    inp = map(parse_game, inp)
    possible_games = filter(lambda g: possible(g, bag), inp)
    return sum(p.gid for p in possible_games)


def solve_2(inp: list[str]):
    inp = map(parse_game, inp)
    inp = map(min_cubes, inp)
    inp = map(lambda d: reduce(operator.mul, d.values()), inp)
    return sum(inp)


if __name__ == "__main__":
    print(solve_1(test_case_1))
    print(solve_1(inp))

    print(solve_2(test_case_2))
    print(solve_2(inp))
