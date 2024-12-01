
from utils.file import read_lines

input_file = "input.txt"

def run():
    input_lines = read_lines(__file__, input_file_name=input_file)
    col_1: list[str] = []
    col_2: list[str] = []

    for line in input_lines:
        split = line.split()
        col_1.append(int(split[0]))
        col_2.append(int(split[1]))

    col_1.sort()
    col_2.sort()

    sim_score = 0

    for val_1 in col_1:
        tally = 0
        for val_2 in col_2:
            if val_1 == val_2:
                tally+=1
            if val_2 > val_1:
                break

        sim_score += calc_sim_score(val_1, tally)

    print(sim_score)

def calc_sim_score(value: int, num_occurances: int) -> int:
    return value * num_occurances

def main():
    run()

if __name__=="__main__":
    main()