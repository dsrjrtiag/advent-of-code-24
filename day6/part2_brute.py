from enum import Enum
from multiprocessing import Pool
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

    not_obstacles = []

    for index, line in enumerate(input_lines):
        find_direction = re.findall("[\^<>v]", line)

        for char_index, char in enumerate(line):
            if char == '.':
                not_obstacles.append((char_index, index))
        if len(find_direction) > 0:
            direction = find_direction[0]
            coord = line.find(direction), index
            direction = direction_map[direction]

    overlaps = []
    args = []
    for new_obstacle in not_obstacles:
        args.append([input_lines, direction, coord, new_obstacle])

    pool = Pool()
    overlaps = list(pool.starmap(check_for_overlap, args))
    # for new_obstacle in not_obstacles:
    #     overlaps.append(check_for_overlap(input_lines, direction, coord, new_obstacle))

    # distinct = set(coords)

    print(sum(overlaps))

def check_for_overlap(input_lines, direction, coord, new_obstacle):
    
    boundaries = [-1, len(input_lines)]
    coords = []
    while True:
        if coord[0] in boundaries or coord[1] in boundaries:
            return 0

        next_coord = coord[0] + direction.value[0], coord[1] + direction.value[1]

        if next_coord[0] in boundaries or next_coord[1] in boundaries:
            return 0
        
        if (coord, direction) in coords:
            return 1
        
        coords.append((coord, direction))

        if input_lines[next_coord[1]][next_coord[0]] == '#' or next_coord == new_obstacle:
            direction = next_direction_map[direction]

        next_coord = coord[0] + direction.value[0], coord[1] + direction.value[1]

        coord = next_coord



def main():
    run()

if __name__=="__main__":
    main()