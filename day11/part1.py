from dataclasses import dataclass
from typing import Self
from utils.file import read_lines
from utils.input_processing import int_values

input_file = "input.txt"

class Value():
    initial_value: int
    current_value: int
    splits: int = 0

    def __init__(self, initial_value: int):
        self.initial_value = initial_value
        self.current_value = initial_value

    @property
    def digits(self) -> int:
        return len(str(self.current_value))

    def blink(self) -> list[Self]:
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

    for blink in range(max_blinks):
        new_values = []
        for value in values:
            new_values.extend(value.blink())
        values = new_values

    print(len([value.initial_value for value in values]))
    
def main():
    run()

if __name__=="__main__":
    main()