import argparse

def parser_file():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='First file to compare')
    parser.add_argument('second_file', help='Second file to compare')
    parser.add_argument(
        '-f',
        '--format',
        default='stylish',
        help='set format of output',    
    )
    args = parser.parse_args()


def main():
    parser_file()

if __name__ == "__main__":
    main()

