from functools import partial
from inputs.get_input import get_inp

test_case_1, test_case_2, inp = get_inp(__file__)

Card = tuple[int, tuple[int], tuple[int]]


def parse_line(line: str):
    card_num, nums = line.split(":")
    card_num = int(card_num.split()[1].strip())
    winning, have = list(map(str.strip, nums.strip().split("|")))
    winning = set(map(lambda num: int(str.strip(num)), winning.split()))
    have = tuple(map(lambda num: int(str.strip(num)), have.split()))
    return card_num, winning, have


def calculate_points(card: Card):
    _, winning, have = card
    n = len(set(winning).intersection(set(have)))
    return 2 ** (n - 1) if n else 0


def add_copy_cards(card: Card, cards: list[Card]):
    card_num, _, _ = card
    points = calculate_points(card)
    return [card] + cards[card_num + 1 : card_num + 1 + points]


def get_cards_count(cards: list[Card], cards_count: dict[int, int]):
    if not cards:
        return cards_count
    card = cards.pop(0)
    card_num, winning, have = card
    cards_count[card_num] = 1 + cards_count.get(card_num, 0)
    matches = len(set(winning).intersection(set(have)))
    for i in range(card_num + 1, card_num + 1 + matches):
        cards_count[i] = cards_count.get(i, 0) + cards_count[card_num]
    return get_cards_count(cards, cards_count)


def solve_1(inp: list[str]):
    cards = map(parse_line, inp)
    points = map(calculate_points, cards)
    return sum(points)


def solve_2(inp: list[str]):
    cards = list(map(parse_line, inp))
    cards_count = get_cards_count(cards, {})
    return sum(cards_count.values())


if __name__ == "__main__":
    print(solve_1(test_case_1))
    print(solve_1(inp))

    print(solve_2(test_case_2))
    print(solve_2(inp))
