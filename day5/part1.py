from utils.file import read_lines

input_file = "input.txt"

def run():
    input_lines = read_lines(__file__, input_file_name=input_file)

    # map of value to sets of values less than and greater than the value
    rule_dict: dict[int, tuple[set,set]] = {}
    middle_nums = []

    process_rules = True
    for input_line in input_lines:
        if process_rules:
            if input_line == '':
                process_rules = False
            else:
                values = list(map(int, input_line.strip().split("|")))
                existing = rule_dict.setdefault(values[0], (set(), {values[1]}))
                existing[1].add(values[1])

                existing = rule_dict.setdefault(values[1], ({values[0]}, set()))
                existing[0].add(values[0])
            
        else:
            values = list(map(int, input_line.strip().split(",")))

            for index, value in enumerate(values):
                valid = True
                before_values = rule_dict[value][0].intersection(values)
                for before_value in before_values:
                    before_index = values.index(before_value)
                    if index < before_index:
                        valid = False
                        break
                if valid is False:
                    break
                greater_than_values = rule_dict[value][1].intersection(values)
                for greater_than_value in greater_than_values:
                    greater_than_index = values.index(greater_than_value)
                    if index > greater_than_index:
                        valid = False
                        break
                if valid is False:
                    break
            
            if valid:
                middle_index = round((len(values) - .25)/2)
                middle_nums.append(values[middle_index])

    print(sum(middle_nums))

def main():
    run()

if __name__=="__main__":
    main()