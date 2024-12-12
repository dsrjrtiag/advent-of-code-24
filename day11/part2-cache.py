from dataclasses import dataclass
from functools import cache
from typing import Self
from utils.file import read_lines
from utils.input_processing import int_values

input_file = "input.txt"

def run():
    inputs = read_lines(__file__, input_file)

    input_line = inputs[0]

    values = [int(text.strip()) for text in input_line.split()]

    max_blinks = 75

    stones = run_blinks(values=tuple(values), blinks_left=max_blinks)

    print(stones)

@cache
def run_blinks(values: list[int], blinks_left: int) -> int:
    count = 0
    if blinks_left == 0:
        return len(values)

    for value in values:
        new_values = []
        new_values.extend(blink(value))
        count += run_blinks(tuple(new_values), blinks_left - 1)

    return count

def blink(value: int):
    if value == 0:
        return [1]
    digits = len(str(value))
    if digits % 2 == 0:
        # even
        first = int(str(value)[:int(digits / 2)])
        second = int(str(value)[int(digits / 2):])
        return [first, second]
    value = value * 2024
    return [value]
    
def main():
    run()

if __name__=="__main__":
    main()