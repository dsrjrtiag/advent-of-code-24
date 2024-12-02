
from utils.file import read_lines
from utils.input_processing import int_values

input_file = "input.txt"

def run():
    input_lines = read_lines(__file__, input_file_name=input_file)

    processed_input = list(map(int_values, input_lines))

    processed_values = list(map(safe, processed_input))

    print(processed_values.count(True))


def safe(levels: list[str]) -> bool:
    prev = levels[0]
    ascending: bool = None
    
    for level in levels[1:]:
        if not safe_sum(prev, level):
            return False
        
        current_ascending = prev - level < 0

        if ascending is None:
            ascending = current_ascending
        else:
            if current_ascending != ascending:
                return False
        
        prev = level

    return True

def safe_sum(first: int, second: int) -> bool:
    diff = abs(first - second)
    return diff >= 1 and diff <= 3

def main():
    run()

if __name__=="__main__":
    main()