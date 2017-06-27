#!/usr/bin/env python
"""
SIM grapher CLI script to create aggregate simulation
run graphs.

Manages options for creating SIM graph using matplotlib.

@author: Kate Stowell and Travis Lanham
"""
from sim_grapher import SimGrapher
import argparse

parser = argparse.ArgumentParser(description='Process grapher args.')

parser.add_argument('-t', '--title', type=str, required=True,
                    help='Title of graph.')
parser.add_argument('-x', '--xaxis', type=str, required=False,
                    default='Offered Load (%)', help='Label for x-axis.')
parser.add_argument('-y', '--yaxis', type=str, required=False,
                    default='Avg Cell Latency (Cells)',
                    help='Label for y-axis.')
parser.add_argument('-o', '--output', type=str, required=True,
                    help='Output file path to save graph (format is png).')
parser.add_argument('-i', '--input', type=str, required=True, nargs='+',
                    help='''Space separated list of input file paths for
                            plotting (must have at least 1).''')

args = parser.parse_args()


if __name__ == '__main__':
    grapher = SimGrapher()
