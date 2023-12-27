from pathlib import Path
import requests


def fetch_input(day: int, cookie: str):
    headers = {"cookie": cookie}
    url = f"https://adventofcode.com/2023/day/{day}/input"
    return requests.get(url, headers=headers).text


def process_input(inp: str):
    return [line for line in inp.split("\n") if line]


def get_and_save_input(day: int):
    filename = f"inputs/files/{day}"
    p = Path(filename)
    p.parents[0].mkdir(parents=True, exist_ok=True)

    plain_text_input = ""
    try:
        plain_text_input = p.read_text()
    except FileNotFoundError as e:
        print("file not yet saved", e)

    if not plain_text_input:
        try:
            import os
            from dotenv import load_dotenv

            load_dotenv()
            cookie = os.environ["COOKIE"]

            plain_text_input = fetch_input(day, cookie)
            p.write_text(plain_text_input)

        except Exception as e:
            print("file not yet saved, and could'nt fetch file", e)
            raise e

    return process_input((plain_text_input))


def get_test_cases_and_input(day: int):
    test_cases = {
        1: (
            "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet",
            "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n"
            "4nineeightseven2\nzoneight234\n7pqrstsixteen\n",
        ),
        2: (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ),
        3: (
            "467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598..",
        ),
        4: (
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\nCard 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\nCard 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\nCard 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\nCard 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        ),
        5: (
            "seeds: 79 14 55 13\n\nseed-to-soil map:\n50 98 2\n52 50 48\n\nsoil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15\n\nfertilizer-to-water map:\n49 53 8\n0 11 42\n42 0 7\n57 7 4\n\nwater-to-light map:\n88 18 7\n18 25 70\n\nlight-to-temperature map:\n45 77 23\n81 45 19\n68 64 13\n\ntemperature-to-humidity map:\n0 69 1\n1 0 69\n\nhumidity-to-location map:\n60 56 37\n56 93 4",
        ),
    }

    t = test_cases.get(int(day), ("nothing... yet",))
    if len(t) == 1:
        t = (t[0], t[0])
    return process_input(t[0]), process_input(t[1]), get_and_save_input(day)


def get_inp(f):
    day = Path(f).stem
    return get_test_cases_and_input(day)
