import re
from utils.file import read_lines
from utils.input_processing import int_values

input_file = "input.txt"
valid_names = "[\w]"

def run():
    input_lines = read_lines(__file__, input_file_name=input_file)

    character_coord_map: dict[str, list[tuple[int, int]]] = parse_inputs(input_lines)

    max_bounds = len(input_lines)
    anti_nodes: set[tuple[int, int]] = []
    all_coords = []

    for coord_map in (character_coord_map.items()):
        coords = coord_map[1]
        for index, coord in enumerate(coords):
            all_coords.append(coord)
            for compare_coord in coords[index + 1:]:
                anti_nodes.extend(compare_coords(coord, compare_coord))

    valid_anti_nodes = list(filter(lambda anti_node: in_bounds(anti_node, max_bounds), anti_nodes))

    print_anti_nodes(valid_anti_nodes, input_lines)
    print(len(set(valid_anti_nodes)))

def compare_coords(coord: tuple[int, int], compare_coord: tuple[int, int]) -> list[tuple[int, int]]:
    diff_x = coord[0] - compare_coord[0]
    diff_y = coord[1] - compare_coord[1]

    anti_node_pos = (coord[0] + diff_x, coord[1] + diff_y)
    anti_node_neg = (compare_coord[0] - diff_x, compare_coord[1] - diff_y)

    return [anti_node_pos, anti_node_neg]

def in_bounds(coord: tuple[int, int], max_bound: int):
    return coord[0] >= 0 and coord[0] < max_bound and coord[1] >= 0 and coord[1] < max_bound

    
def parse_inputs(input_lines: list[str]):
    char_coord_map: dict[str, list[tuple[int, int]]] = {}
    for y, line in enumerate(input_lines):
        for x, character in enumerate(line): 
            if len(re.findall(valid_names, character)) > 0:
                coords = char_coord_map.get(character, [])
                coords.append((x, y))
                char_coord_map[character] = coords
    return char_coord_map

def print_anti_nodes(anti_nodes, input_lines):
    for y in range(len(input_lines)):
        for x in range(len(input_lines)):
            if (x, y) in anti_nodes:
                print("#", end='')
            else:
                orig_char = input_lines[y][x]
                if orig_char == "#":
                    orig_char = '.'
                print(orig_char, end='')
        print()

def main():
    run()

if __name__=="__main__":
    main()