from dataclasses import dataclass
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

    # map of values, and how many blinks it takes to split
    blink_map: dict[int, int] = {}
    # map of values, and the second blink it occurred
    occurrence_map: dict[int, int] = {}

    max_blinks = 25

    for blink in range(max_blinks):
        new_values = []
        for value in values:
            blink_results = value.blink()
            if len(blink_results) > 1:
                # split
                
                blinks_to_split = value.blinks
                occurred_before = value.initial_value in blink_map.keys()
                blink_map[value.initial_value] = blinks_to_split
                if value.initial_value == 1:
                    print("break")
                if occurred_before:
                    if max_blinks - blink > blinks_to_split:
                        # can occur again
                        occurrence_map[value.initial_value] = blink

                for blink_value in blink_results:
                    occurred_before = blink_value.initial_value in blink_map.keys()

                    if occurred_before:
                        blink_results.remove(blink_value)
            new_values.extend(blink_results)
        values = new_values
        print(f"blink {blink} complete")


    print(len([value.initial_value for value in values]))
    print([value.current_value for value in values])

    # for each occurence in occurence map
        # get the # of blinks in blink map to split
            #  for the blinks after the initial blink, calculate how many times it would have split ^ 2 to calculate splits

    pebbles = len(values) + ""
    
    
def main():
    run()

if __name__=="__main__":
    main()