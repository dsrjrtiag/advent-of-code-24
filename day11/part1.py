from dataclasses import dataclass
from utils.file import read_lines
from utils.input_processing import int_values

input_file = "input.txt"

class Value():
    initial_value: int
    digits: int
    splits: int = 0

    def __init__(self, initial_value: int):
        self.initial_value = initial_value
        self.digits  = len(str(initial_value))

def run():
    inputs = read_lines(__file__, input_file)

    input_line = inputs[0]

    values = [Value(initial_value = int(text.strip())) for text in input_line.split()]

    max_blinks = 25

    for blink in range(max_blinks):
        new_values = []
        for value in values:
            new_values.append(value.split())
        values = new_values

    print([value.initial_value for value in values])
    
def main():
    run()

if __name__=="__main__":
    main()