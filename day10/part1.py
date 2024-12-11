from dataclasses import dataclass
from utils.file import read_lines
from utils.input_processing import int_values

input_file = "input.txt"

@dataclass
class Coord:
    x: int
    y: int

def run():
    input_lines = read_lines(__file__, input_file_name=input_file)
    input_ints = [list(map(int, input_line)) for input_line in input_lines]

    trailheads = find_trailheads(input_ints)
    max = len(input_lines) - 1

    valid_trails = [get_trails(trailhead, max, input_ints) for trailhead in trailheads]

    print(valid_trails)

def score(path: list[Coord]) -> int:
    sum(map(get_height))

def get_trails(trailhead: Coord, max: int, input_ints: list[list[int]], stops: int = 0) -> int:
    stops += 1
    head_height = get_height(trailhead, input_ints)

    if head_height == 9:
        return 1

    coords_to_check = get_surrounding(trailhead, max)
    valid_paths = list(filter(lambda coord: get_height(coord, input_ints) == head_height + 1, coords_to_check))

    if len(valid_paths) > 0:
        path_count = 0
        for valid_coord in valid_paths:
            path_count += get_trails(valid_coord, max, input_ints, stops)
        return path_count
    else:
        return 0

def get_height(coord: Coord, input_ints: list[list[int]]):
    return input_ints[coord.y][coord.x]

def get_surrounding(coord: Coord, max: int) -> list[Coord]:
    coords = []
    if coord.x > 0:
        coords.append(Coord(coord.x - 1, coord.y))
    if coord.x < max:
        coords.append(Coord(coord.x + 1, coord.y))
    if coord.y > 0:
        coords.append(Coord(coord.x, coord.y - 1))
    if coord.y < max:
        coords.append(Coord(coord.x, coord.y + 1))
    return coords


def find_trailheads(grid: list[list[int]]) -> list[Coord]:
    coords = []
    for y, line in enumerate(grid):
        for x, value in enumerate(line):
            if value == 0:
                coords.append(Coord(x, y))

    return coords

    
def main():
    run()

if __name__=="__main__":
    main()