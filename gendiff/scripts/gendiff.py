#!/usr/bin/env python
from gendiff.cli import parse_arguments
from gendiff.generate import generate_gendiff


def main():
    paths = parse_arguments()
    file_path1 = paths.first_file
    file_path2 = paths.second_file
    print(generate_gendiff(file_path1, file_path2))


if __name__ == "__main__":
    main()
