from dataclasses import dataclass
import re
from utils.file import read_lines
from utils.input_processing import int_values

input_file = "input.txt"
valid_names = "[\w]"

@dataclass
class Spot:
    name: str
    num_of_spaces: int
    is_gap: bool

def run():
    input_lines = read_lines(__file__, input_file_name=input_file)
    input = input_lines[0]

    spaces: list[Spot] = []
    gap_name_count = 0
    space_name_count = 0

    for index, character in enumerate(input):
        is_gap = index % 2 != 0
        num_of_spaces = int(character)
        
        if is_gap:
            name = str(gap_name_count)
            gap_name_count += 1
        else:
            name = str(space_name_count)
            space_name_count += 1

        spaces.append(Spot(name=name, num_of_spaces=num_of_spaces, is_gap=is_gap))


    only_files = list(filter(lambda spot: not spot.is_gap, spaces))
    expand_files = []
    for file in only_files:
        for i in range(file.num_of_spaces):
            expand_files.append(file.name)

    file_value_queue = list(expand_files)

    output = []
    for spot in spaces:
        if len(file_value_queue) == 0:
            break
        if spot.is_gap:
            for i in range(spot.num_of_spaces):
                output.append(file_value_queue.pop())
        else:
            for i in range(spot.num_of_spaces):
                if len(file_value_queue) == 0:
                    break
                output.append(file_value_queue.pop(0))
            
    print(''.join(output))

    checksum = 0
    for index, name in enumerate(output):
        checksum += index * int(name)

    print(checksum)

    
def main():
    run()

if __name__=="__main__":
    main()