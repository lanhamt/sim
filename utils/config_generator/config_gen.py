#!/usr/bin/env python
"""
SIM configuration file generator CLI script.

Manages options for generating a new SIM config
file.

@author: Kate Stowell and Travis Lanham
"""
from sim_config_generator import SimConfigGenerator
import argparse

parser = argparse.ArgumentParser(description='Process config generator args.')

parser.add_argument('-i', '--input', type=str, required=True,
                    help='Path to input template to base config on.')
parser.add_argument('-o', '--output', type=str, required=True,
                    help='''Output directory path for new config file, do
                            not include filename.''')
parser.add_argument('-r', '--range', type=int, nargs=2, required=True,
                    help='''Load range (exclusive upper bound), separate
                            minimum load and maximum with space following this
                            flag (values are out of 100, given as percentage).
                         ''')
parser.add_argument('-d', '--load_delta', type=int, default=1,
                    help='''Load delta (amount to increase load from minimum
                            load up to maximum), default is 1.''')
parser.add_argument('-c', '--iter_count', type=int, default=0,
                    help='Number of iterations (if applicable) for algorithm.')

args = parser.parse_args()


def parse_input_path(path):
    """Parse input filename from input path.

        Args:
            path (str): Path to input template to base config on.
                Assumes that path does not have trailing '/'.

        Returns:
            str: Filename, excluding path.
        """
    if '/' in path:
        return path.split('/')[-1]
    else:
        return path


if __name__ == '__main__':
    input_path = args.input
    output_path = args.output
    iter_count = args.iter_count
    min_load = args.range[0]
    max_load = args.range[1]
    delta = args.load_delta

    input_filename = parse_input_path(input_path)

    if not output_path.endswith('/'):
        output_path += '/'

    for load in range(min_load, max_load, delta):
        out_file = str(load) + '.' + input_filename
        out_path = output_path + out_file
        scg = SimConfigGenerator(input_path, out_path, load, iter_count)
        scg.open_file_paths()
        scg.process_file()
