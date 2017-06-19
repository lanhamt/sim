# SIM Config File Generator

## Purpose
Creating performance graphs for load vs latency involves many runs of SIM
with different offered loads for the input arbiters. The `config_gen.py`
script uses a master config template to generate additional config files with
varying loads.

## Usage

```
$ python config_gen.py -i INPUT -o OUTPUT -r RANGE RANGE [-d LOAD_DELTA]
                       [-c ITER_COUNT]

$ python config_gen.py -i example/16x16.slip.u \ 
                       -o example/islip_configs/ -r 0 101 -d 2
```
The above command uses master template in `example/16x16.slip.u` to generate
load configs from 0 to 100 with an interval of 2 (0, 2, 4, ... 100), and
outputs new configs in `example/islip_configs/`.

The naming convention takes the load and appends the master config file used
as a template. Using the example above, the first config file generated is
for load 0 with `16x16.slip.u` as the master config, resulting in the new
configuration file `0.16x16.slip.u`.
