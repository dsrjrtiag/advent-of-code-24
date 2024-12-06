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
    past_coords = []
    coords = []
    obstacles = []

    for index, line in enumerate(input_lines):
        obstacle_indexs = [i for i, x in enumerate(line) if x == "#"]
        for obstacle_index in obstacle_indexs:
            obstacles.append((obstacle_index, index))

        find_direction = re.findall("[\^<>v]", line)
        if len(find_direction) > 0:
            direction = find_direction[0]
            coord = line.find(direction), index
            direction = direction_map[direction]


    start = coord
    start_direction = direction

    boundaries = [-1, len(input_lines)]
    turns = []
    blocks = []

    while True:
        if coord[0] in boundaries or coord[1] in boundaries:
            break

        # coords.append((coord, direction))
        coords.append(coord)

        next_coord = coord[0] + direction.value[0], coord[1] + direction.value[1]



        # if len(turns)  > -1:
        if direction == Direction.LEFT:
            for obstacle in obstacles:
                if coord[0] == obstacle[0] and coord[1] > obstacle[1]:
                    intersection = (obstacle[0], obstacle[1] + 1)
                    if intersection in coords:
                    # if (intersection, Direction.RIGHT) in coords  or (intersection, Direction.UP) in coords:
                        # if(obstacle[0] + 1, obstacle[1] + 1 ) in coords:
                        blocks.append(next_coord)
                        break
        if direction == Direction.RIGHT:
            for obstacle in obstacles:
                if coord[0] == obstacle[0] and coord[1] < obstacle[1]:
                    intersection = (obstacle[0], obstacle[1] - 1)
                    if intersection in coords:
                    # if (intersection, Direction.LEFT) in coords or (intersection, Direction.DOWN) in coords:
                        # if (obstacle[0] - 1, obstacle[1] - 1) in coords:
                        blocks.append(next_coord)
                        break
        if direction == Direction.UP:
            for obstacle in obstacles:
                if coord[1] == obstacle[1] and coord[0] < obstacle[0]:
                    intersection = (obstacle[0] - 1, obstacle[1])
                    if intersection in coords:
                    # if (intersection, Direction.DOWN) in coords or (intersection, Direction.RIGHT) in coords:
                        # if(obstacle[0] - 1, obstacle[1] + 1) in coords:
                        blocks.append(next_coord)  
                    break
        if direction == Direction.DOWN:
            for obstacle in obstacles:
                if coord[1] == obstacle[1] and coord[0] > obstacle[0]:
                    intersection = (obstacle[0] + 1, obstacle[1])
                    if intersection in coords:
                    # if (intersection, Direction.UP) in coords or (intersection, Direction.LEFT) in coords:
                        # if (obstacle[0] + 1, obstacle[1] - 1) in coords:
                        blocks.append(next_coord)
                        break

        if next_coord[0] in boundaries or next_coord[1] in boundaries:
            break

        if input_lines[next_coord[1]][next_coord[0]] == '#':
            obstacles.append(next_coord)
            turns.append(coord)
            direction = next_direction_map[direction]

        next_coord = coord[0] + direction.value[0], coord[1] + direction.value[1]

        coord = next_coord

    # distinct = set(past_coords)

    print(len(blocks))
    print(1516)

    # for y in range(len(input_lines)):
    #     line = ''
    #     for x in range(len(input_lines)):
    #         symbol = ''
    #         if (x, y) in coords:
    #             symbol = "-"
    #         else:
    #             symbol = input_lines[y][x]
    #         if (x, y) in turns:
    #             symbol = "+"
    #         if (x, y) in blocks:
    #             symbol = "0"


    #         line += symbol

    #     print(line)

def main():
    run()

if __name__=="__main__":
    main()