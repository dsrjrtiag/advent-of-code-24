from utils.file import read_lines

input_file = "input.txt"

def run():
    input_lines = read_lines(__file__, input_file_name=input_file)

def main():
    run()

if __name__=="__main__":
    main()