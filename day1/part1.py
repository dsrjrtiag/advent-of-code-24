
from utils.file import read_lines

input_file = "input.txt"

def run():
    input_lines = read_lines(__file__, input_file_name=input_file)
    col_1: list[str] = []
    col_2: list[str] = []

    for line in input_lines:
        split = line.split()
        col_1.append(split[0])
        col_2.append(split[1])

    col_1.sort()
    col_2.sort()

    diff = 0

    for index, val_1 in enumerate(col_1):
        diff += abs(int(val_1) - int(col_2[index]))

    print(diff)

def main():
    run()

if __name__=="__main__":
    main()