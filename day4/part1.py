
from math import sqrt
import re
from utils.file import read_lines

input_file = "input.txt"
regex = "XMAS"

def run():
    input_lines = read_lines(__file__, input_file_name=input_file)


    total = sum(map(horizontal, input_lines))
    total += vertical(input_lines=input_lines)
    total += diagonal(input_lines=input_lines)

    print(total)

def diagonal(input_lines: list[str]):

    diagonals = get_diagonal_lines(input_lines)

    backslash = sum(map(horizontal, diagonals))

    backwards_inputs = []
    for input in input_lines:
        backwards_inputs.append(input[::-1])

    diagonals_bw = get_diagonal_lines(backwards_inputs)
    forwards_slash = sum(map(horizontal, diagonals_bw))

    return backslash + forwards_slash

def get_diagonal_lines(input_lines):
    diagonals = []
    num_columns = len(input_lines)
    num_rows = len(input_lines[0])

    for z in range(num_rows):
        y = num_columns - 1 - z

        diagonal = ''
        for x in range(0, num_columns - y):
            coord = x, y + x
            diagonal += input_lines[coord[1]][coord[0]]
        diagonals.append(diagonal)

    for z in range(num_rows):        
        diagonal = ''
        for x in range(z+1, num_rows):
            coord = x, x - z - 1
            diagonal += input_lines[coord[1]][coord[0]]
        diagonals.append(diagonal)


    return diagonals

def vertical(input_lines: list[str]):
    verticals = []

    for x in range(len(input_lines[0])):
        vertical = ''
        for line in input_lines:
            vertical += line[x]
        verticals.append(vertical)

    return sum(map(horizontal, verticals))

def horizontal(input: str) -> int:
    forwards = re.findall(regex, input)
    reversed = input [::-1]
    backwards = re.findall(regex, reversed)

    return len(forwards) + len(backwards)

def main():
    run()

if __name__=="__main__":
    main()