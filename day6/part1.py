from enum import Enum
import re
from utils.file import read_lines

input_file = "input.txt"


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

direction_map = {"^": Direction.UP,
                 "<": Direction.LEFT,
                 ">": Direction.RIGHT,
                 "v": Direction.DOWN}

next_direction_map = {Direction.UP: Direction.RIGHT,
                      Direction.RIGHT: Direction.DOWN,
                      Direction.DOWN: Direction.LEFT,
                      Direction.LEFT: Direction.UP}

def run():
    input_lines = read_lines(__file__, input_file_name=input_file)
    coords = []

    for index, line in enumerate(input_lines):
        find_direction = re.findall("[\^<>v]", line)
        if len(find_direction) > 0:
            direction = find_direction[0]
            coord = line.find(direction), index
            direction = direction_map[direction]
            break

    boundaries = [-1, len(input_lines)]

    while True:
        # if len(coords) == 39:
        #     print("Debug")
        if coord[0] in boundaries or coord[1] in boundaries:
            break


        coords.append(coord)

        next_coord = coord[0] + direction.value[0], coord[1] + direction.value[1]

        if next_coord[0] in boundaries or next_coord[1] in boundaries:
            break

        if input_lines[next_coord[1]][next_coord[0]] == '#':
            direction = next_direction_map[direction]

        next_coord = coord[0] + direction.value[0], coord[1] + direction.value[1]

        coord = next_coord

    distinct = set(coords)

    print(len(distinct))



def main():
    run()

if __name__=="__main__":
    main()