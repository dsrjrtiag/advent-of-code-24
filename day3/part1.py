
import re
from utils.file import read_lines
from utils.input_processing import int_values

input_file = "input.txt"

def run():
    input_lines = read_lines(__file__, input_file_name=input_file)

    def parse_mul(input: str):
        return re.compile("mul\(\d*,\d*\)").findall(input)

    parsed_input = sum(list(map(parse_mul, input_lines)), [])

    def get_values(input: str) -> tuple[int, int]:
        numbers = re.compile("\d+").findall(input)

        return int(numbers[0]), int(numbers[1])

    value_pairs = list(map(get_values, parsed_input))

    def multiply(input: tuple[int, int]) -> int:
        return input[0] * input[1]

    multiplied_values = list(map(multiply, value_pairs))

    print(sum(multiplied_values))

def main():
    run()

if __name__=="__main__":
    main()