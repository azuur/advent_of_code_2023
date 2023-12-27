from functools import partial
import math
from inputs.get_input import get_inp

test_case_1, test_case_2, inp = get_inp(__file__)


def parse_input(inp: list[str]):
    seeds = [int(x) for x in inp.pop(0).split()[1:]]
    maps = []
    _map = None
    for line in inp:
        if not line[0].isdigit():
            maps.append(_map)
            from_to = line.split()[0].split("-")
            _from, to = from_to[0], from_to[-1]
            _map = {"from": _from, "to": to, "ranges": []}
            continue
        destination_start, source_start, length = list(map(int, line.split()))
        _map["ranges"].append((destination_start, source_start, length))
    maps.append(_map)
    maps = maps[1:]
    return seeds, maps


def follow_map(source_value: int, ranges: tuple[int, int, int]):
    for rnge in ranges:
        dst_start, src_start, length = rnge
        k = src_start - source_value
        m = src_start + length - 1 - source_value
        if k * m <= 0:
            return dst_start - k
    return source_value


def follow_maps_to_location(
    source_value: int, maps: list[dict], source: str, destination: str
):
    if source == destination:
        return source_value
    relevant_maps = [_map for _map in maps if _map["from"] == source]
    direct_maps = [_map for _map in relevant_maps if _map["to"] == "location"]
    relevant_maps = direct_maps if direct_maps else relevant_maps
    if not relevant_maps:
        return math.inf
    other_maps = [_map for _map in maps if _map["from"] != source]
    results = []
    for _map in relevant_maps:
        new_value = follow_map(source_value, _map["ranges"])
        result = follow_maps_to_location(
            new_value, other_maps, _map["to"], destination
        )
        results.append(result)
    return min(results)


def solve_1(inp: list[str]):
    seeds, maps = parse_input(inp)
    _loc = partial(
        follow_maps_to_location,
        maps=maps,
        source="seed",
        destination="location",
    )
    return min(map(_loc, seeds))


def solve_1(inp: list[str]):
    seeds, maps = parse_input(inp)
    seeds = list(range(seeds[0], seeds[0] + seeds[1]))
    seeds.extend(range(seeds[2], seeds[2] + seeds[3]))
    seeds = set(seeds)
    _loc = partial(
        follow_maps_to_location,
        maps=maps,
        source="seed",
        destination="location",
    )
    return min(map(_loc, seeds))


if __name__ == "__main__":
    print(solve_1(test_case_1))
    print(solve_1(inp))

    # print(solve_2(test_case_2))
    # print(solve_2(inp))
