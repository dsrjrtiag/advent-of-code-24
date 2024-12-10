from dataclasses import dataclass
from utils.file import read_lines
from utils.input_processing import int_values

input_file = "input.txt"

def run():
    input_lines = read_lines(__file__, input_file_name=input_file)
    input_ints = list(map(int_values, input_lines))

    trailheads = find_trailheads(input_ints)

    for head in trailheads:
        

    print(checksum)

@dataclass
class Coord:
    x: int
    y: int

def find_trailheads(grid: list[list[int]]) -> list[Coord]:
    coords = []
    for y, line in enumerate(grid):
        for x, value in line:
            if value == 0:
                coords.append(x, y)

    
def main():
    run()

if __name__=="__main__":
    main()