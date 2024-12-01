from io import TextIOWrapper
from pathlib import Path


def read_lines(module_file: str, input_file_name: str) -> list[str]:
    p = Path(module_file).with_name(input_file_name)

    with p.open('r') as f:
        return f.readlines()
