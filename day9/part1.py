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
    file_values = ''
    for file in only_files:
        file_values += (str(file.name) * file.num_of_spaces)

    file_value_list = list(file_values)

    output = ''
    for spot in spaces:
        if len(file_value_list) == 0:
            break
        if spot.is_gap:
            for i in range(spot.num_of_spaces):
                output += file_value_list.pop()
        else:
            for i in range(spot.num_of_spaces):
                if len(file_value_list) == 0:
                    break
                output += file_value_list.pop(0)
            
    print(output)

    checksum = 0
    for index, character in enumerate(output):
        checksum += index * int(character)

    print(checksum)

    
def main():
    run()

if __name__=="__main__":
    main()