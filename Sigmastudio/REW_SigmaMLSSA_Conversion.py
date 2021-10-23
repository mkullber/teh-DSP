#!/usr/bin/env python3

import sys
import numpy as np

filename_in = sys.argv[1]
filename_out = filename_in.replace('.txt', '_MLSSA.txt')

fin = open(filename_in, 'r+')
fout = open(filename_out, 'w')

# Sigma Studio Required Spacing Placement
fout.write('"Sensitivity Excess Phase - dB SPL/watt (8 ohms, @0.50 meters) (High)"\n')
fout.write('      "Hz"  "Mag (dB)"       "deg"\n')

# Load in data, skip the header.
# REW has 14 lines of header info
data = np.genfromtxt(filename_in, skip_header=14, delimiter=' ')

for i in range(0, len(data)):
    fout.write('{0:10}, {1:11}, {2:11}\n'.format(data[i, 0], data[i, 1], data[i, 2]))

fout.close()

print('Conversion Complete!')
