
from math import sqrt
import re
from utils.file import read_lines

input_file = "input.txt"


def run():
    input_lines = read_lines(__file__, input_file_name=input_file)

    xmasses = 0
    for line_index in range (1, len(input_lines) - 1):
        for char_index in range(1, len(input_lines) - 1):
            if input_lines[line_index][char_index] == 'A':
                mas_found_1 = check_diag_1(input_lines, line_index, char_index)
                mas_found_2 = check_diag_2(input_lines, line_index, char_index)

                xmasses += 1 if mas_found_1 is True and mas_found_2 is True else 0
    print(xmasses)

def check_diag_1(input_lines: list, line_index: int, char_index: int):
    first = input_lines[line_index - 1][char_index - 1]
    second = "A"
    last = input_lines[line_index + 1][char_index + 1]

    if first + second + last == "MAS":
        return True
    
    if last + second + first == "MAS":
        return True

    return False

def check_diag_2(input_lines: list, line_index: int, char_index: int):
    first = input_lines[line_index - 1][char_index + 1]
    second = "A"
    last = input_lines[line_index + 1][char_index - 1]

    if first + second + last == "MAS":
        return True
    
    if last + second + first == "MAS":
        return True

    return False

def main():
    run()

if __name__=="__main__":
    main()