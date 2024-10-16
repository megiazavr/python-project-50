import argparse


def parse_arguments():
    """
    Parses command line arguments.

    Returns:
        Namespace: Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', choices=['stylish', 'plain', 'json'],
                        default='stylish',
                        help='set format of output')
    return parser.parse_args()
