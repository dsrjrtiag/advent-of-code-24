from dataclasses import dataclass
from functools import cache
from typing import Self
from utils.file import read_lines
from utils.input_processing import int_values

input_file = "input.txt"

class Value():
    initial_value: int
    current_value: int
    blinks: int = 0

    def __init__(self, initial_value: int):
        self.initial_value = initial_value
        self.current_value = initial_value

    def __hash__(self):
        return self.initial_value * self.current_value * self.blinks

    @property
    def digits(self) -> int:
        return len(str(self.current_value))

    def blink(self) -> list[Self]:
        self.blinks += 1
        if self.current_value == 0:
            self.current_value = 1
            return [self]
        if self.digits % 2 == 0:
            # even
            first = int(str(self.current_value)[:int(self.digits / 2)])
            second = int(str(self.current_value)[int(self.digits / 2):])
            return [Value(first), Value(second)]
        self.current_value = self.current_value * 2024
        return [self]

def run():
    inputs = read_lines(__file__, input_file)

    input_line = inputs[0]

    values = [Value(initial_value = int(text.strip())) for text in input_line.split()]

    max_blinks = 25

    # stones = 0
    # for value in values:
        # stones += run_blinks(values=tuple([value]), blinks_left = max_blinks)
    stones = run_blinks(values=tuple(values), blinks_left=max_blinks)

    print(stones)

@cache
def run_blinks(values: list[Value], blinks_left: int) -> int:
    count = 0
    for value in values:
        if blinks_left == 0:
            return len(values)
        new_values = []
        new_values.extend(value.blink())
        count += run_blinks(tuple(new_values), blinks_left - 1)

    return count
    
def main():
    run()

if __name__=="__main__":
    main()