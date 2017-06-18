#!/usr/bin/env python
"""
SIM configuration file generator class.

Manages generation of a single new configuration file
based on an existing template file. 

@author: Kate Stowell and Travis Lanham
"""

import sys

TRAFFIC_MODELS = ["bernoulli_iid_uniform", "bernoulli_iid_nonuniform", 
                  "bursty", "bursty_nonuniform", "keepfull", "trace", "null"]

class SimConfigGenerator:

    def __init__(self, in_path, out_path, load, iter_count=0):
        """Initialize config generator.

        Args:
            in_path (str): Path to input template to base config on.
            out_path (str): Output file path for new config file.
            load (int): Input load for each switch input arbiter.
            iter_count (int): Number of iterations (if applicable) for 
                algorithm.
        """
        self._input_file_path = in_path
        self._output_file_path = out_path
        self._load = load
        self._iteration_count = iter_count
        self._input_fd = None
        self._output_fd = None

    def open_file_paths(self):
        """Opens paths to input template file and output
        path for new config file that will be generated.

        Raises:
            IOError: if input file and output path cannot be opened
        """
        try:
            self._input_fd = open(self._input_file_path, 'r')
            self._output_fd = open(self._output_file_path, 'w+')
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)

    def process_file(self):
        """TODO
        """
        switch_num = 0
        for line in self._input_fd:
            new_line = line

            is_switch_line, traffic_model = is_line_switch_config(line)
            if is_switch_line:
                # The traffic model name will be in the config lines
                # for specifying an input load.
                new_line = '  ' + str(switch_num) + ' ' + traffic_model + \
                           '  -u 0.' + str(self._load)
                switch_num += 1
            elif 'Algorithm' in line and not self._iteration_count == 0:
                line_tokens = line.split(' ')
                iter_token_index = line_tokens.index('-n')
                good = line_tokens[:iter_token_index + 1]
                good.append(str(self._iteration_count))
                new_line = '  ' + ' '.join(good)

            self._output_fd.write(new_line)

    def is_line_switch_config(self, line):
        """TODO
        """
        for model in TRAFFIC_MODELS:
            if model in line:
                return True, model
        return False, ""
