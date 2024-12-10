from dataclasses import dataclass
import re
from utils.file import read_lines
from utils.input_processing import int_values

input_file = "input.txt"
valid_names = "[\w]"

@dataclass
class File:
    name: int
    spaces: int

@dataclass
class Gap:
    name = 0
    spaces:int

def run():
    input_lines = read_lines(__file__, input_file_name=input_file)
    input = input_lines[0]

    all_files: list[File] = []
    all_spaces = []

    for index, num_spaces in enumerate(input):
        if index % 2 == 0:
            space = File(len(all_files), int(num_spaces))
            all_files.append(space)
        else:
            space = Gap(int(num_spaces))
        all_spaces.append(space)

    empty_spaces = 0
    output: list[int] = []
    for space in all_spaces:
        if isinstance(space, File) :
            if empty_spaces > 0:
                # check if any file will fit in the gap prior to this file
                fit_files = get_fit_files(all_files, empty_spaces)

                while len(fit_files) > 0:
                    max_file = max(fit_files, key=lambda file: file.name)
                    all_files.remove(max_file)
                    max_file_length = max_file.spaces

                    output.extend(space_to_list(max_file))
                    empty_spaces -= max_file_length

                    fit_files = get_fit_files(all_files, empty_spaces)
                if empty_spaces > 0:
                    output.extend(empty_space_to_list(empty_spaces))
                    empty_spaces = 0

            if space not in all_files:
                output.extend(empty_space_to_list(space.spaces))
                empty_spaces = 0
            else:
                output.extend(space_to_list(space))
                all_files.remove(space)
        else:
            empty_spaces += space.spaces

    def checksum(outputs: list[int]) -> int:
        result = 0
        for index, spaces in enumerate(outputs):
            result += index * spaces
        return result

    # str_output = "".join(map(str, output))
    # print(str_output)
    print(checksum(output))


def get_fit_files(file_pool: list[File], gap: int) -> list[File]:
        files_that_fit = []
        for file in file_pool:
            if file.spaces <= gap:
                files_that_fit.append(file)
        return files_that_fit

def space_to_list(space: File | Gap) -> list[int]:
    return [space.name for i in range(space.spaces)]

def empty_space_to_list(spaces: int) -> list[int]:
    return [0 for i in range(spaces)]

def main():
    run()

if __name__=="__main__":
    main()
