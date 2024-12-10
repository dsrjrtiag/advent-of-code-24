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

    count = 0
    name_file_map: dict[int, Spot] = {} 
    spaces_file_map: list[list[Spot]] = [[],
                                         [],
                                         [],
                                         [],
                                         [],
                                         [],
                                         [],
                                         [],
                                         [],
                                         []]
    spaces: list[Spot] = []

    for index, character in enumerate(input):
        in_gap = index % 2 != 0
        name = str(count)
        num_of_spaces = int(character)
        
        spot = Spot(name=name, num_of_spaces=num_of_spaces, is_gap=in_gap)
        spaces.append(spot)

        if in_gap:
            count += 1
        else:
            name_file_map[count] = spot
            spaces_file_map[num_of_spaces].insert(0, spot)
            
    # for space_map in spaces_file_map.items():
    #     space_map[1].sort(key=lambda file: int(file.name), reverse=True)

    only_files = list(name_file_map.values())

    current_gap = 0
    output = ""
    in_gap = False
    for spot in spaces:
        if len(only_files) < 1:
            break
        
        if spot.is_gap and not spot.name.startswith("inserted_gapfor"):
            in_gap = True
            current_gap += spot.num_of_spaces
        if not spot.is_gap or spot.name.startswith("inserted_gapfor"):
            
            # fit_files = list(filter(lambda file:file.num_of_spaces <= current_gap , only_files))
            files_that_fit = get_files_that_fit(spaces_file_map, current_gap)

            files_that_fit.sort(key=lambda file: int(file.name), reverse=True)

            while len(files_that_fit) > 0:
                highest_fit_file = files_that_fit[0]

                output += file_str(output, highest_fit_file)
                current_gap -= highest_fit_file.num_of_spaces
                only_files.remove(highest_fit_file)
                
                spaces.insert((int(highest_fit_file.name) * 2) + 1, Spot(name="inserted_gapfor" + highest_fit_file.name,
                                                                        num_of_spaces=highest_fit_file.num_of_spaces,
                                                                        is_gap=True))
                spaces.remove(highest_fit_file)
                spaces_file_map[highest_fit_file.num_of_spaces].remove(highest_fit_file)
                files_that_fit = get_files_that_fit(spaces_file_map, current_gap)
            if(current_gap > 0):
                empty_spot = Spot("0", current_gap, True)
                output += file_str(output, empty_spot)

            in_gap = False
            current_gap = 0

            if spot.name.startswith("inserted_gapfor"):
                empty_spot = Spot("0", spot.num_of_spaces, True)
                output += file_str(output, empty_spot)

            if spot in only_files:
                output += file_str(output, spot)
                only_files.remove(spot)
    print(output)

    checksum = 0
    for index, character in enumerate(output):
        checksum += index * int(character)

    print("Must be higher than 5012032747613")
    print(checksum)

def get_files_that_fit(spaces_file_map, current_gap):
    fit_file_lists = spaces_file_map[0: current_gap + 1]
    files_that_fit = []

    for index, file_list in enumerate(fit_file_lists):
        if len(file_list)> 0:
            files_that_fit.append(file_list[0])
    return files_that_fit

def file_str(output: str, spot: Spot):
    output = ""
    for i in range(spot.num_of_spaces):
        output += spot.name
    return output
            

def sort_by_name(file_x: Spot, file_y: Spot):
    # names are unique, don't worry about equals
    return int(file_x.name) > int(file_y.name)

    # expand_files = []
    # for file in only_files:
    #     for i in range(file.num_of_spaces):
    #         expand_files.append(file.name)

    # file_value_queue = list(expand_files)

    # output = []
    # current_gap = 0
    # for spot in spaces:
    #     if len(file_value_queue) == 0:
    #         break
    #     if spot.is_gap:
    #         current_gap += 1
    #         for i in range(spot.num_of_spaces):
    #             output.append(file_value_queue.pop())
    #     else:
    #         for i in range(spot.num_of_spaces):
    #             if len(file_value_queue) == 0:
    #                 break
    #             output.append(file_value_queue.pop(0))
            
    print(''.join(output))

    checksum = 0
    for index, name in enumerate(output):
        checksum += index * int(name)

    print(checksum)

    
def main():
    run()

if __name__=="__main__":
    main()