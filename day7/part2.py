from utils.file import read_lines
from utils.input_processing import int_values

input_file = "input.txt"

def run():
    input_lines = read_lines(__file__, input_file_name=input_file)
    inputs = list(map(get_inputs, input_lines))
    
    outputs = []

    for input in inputs:
        target = input[0]
        values = input[1]
        first_value = values[0]

        outputs.append(equal_target(values=values, index=1, target=target, prev_values=[first_value]))    

    print(sum(outputs))

def equal_target(values: list[int], index: int, target: int, prev_values: list[int]) -> int:
    # start at index 1
    is_last_value = len(values) == index + 1
    next_value = values[index]

    valid_values = []

    for prev_value in prev_values:
        sum = prev_value + next_value
        product = prev_value * next_value
        combine = int(str(prev_value) + str(next_value))

        if is_last_value and sum == target:
            return target
        if is_last_value and product == target:
            return target
        if is_last_value and combine == target:
            return target
        if is_last_value:
            continue
        
        if sum <= target:
            valid_values.append(sum)
        if product <= target:
            valid_values.append(product)
        if combine <= target:
            valid_values.append(combine)

    if len(valid_values) == 0:
        return 0
    
    return equal_target(values=values, index=index + 1, target=target, prev_values=valid_values)

def get_inputs(input_line: str) -> tuple[int, list[int]]:
    split = input_line.split(":")
    target = int(split[0].strip())
    values = [int(x.strip()) for x in split[1].split()]

    return (target, values)

def main():
    run()

if __name__=="__main__":
    main()