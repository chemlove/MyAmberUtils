#! /usr/bin/env python

# -*- coding: utf-8 -*-

# Copyright (c) 2018 Martin Rosellen

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import argparse
import sys


def main(argv):
    parser = argparse.ArgumentParser(description='Get mean angle from cpptraj generated stat file.')
    parser.add_argument('angles', help='file containing the statistics generated by cpptraj.')
    args = parser.parse_args()

    angles_file = args.angles
    angles = {}
    with open(angles_file, 'r') as f:
        content = f.readlines()
        last = ""
        mean = ""
        angle = ""
        for a_line in content:
            if "STATISTICS" in a_line and "Hist" not in a_line:
                angle = a_line.split()[1]
            if "Hist" not in last and "AVERAGE" in a_line:
                mean = a_line.split()[1].strip("(")
            last = a_line
            if mean and angle:
                angles[angle] = mean
    if "short" in angles_file:
        outfile = "angles_means_short.dat"
    else:
        outfile = "angles_means_long.dat"

    with open(outfile, 'w') as o:
        for key, value in angles.items():
            o.write('%s %s\n' % (key, value))



if __name__ == "__main__":
    main(sys.argv)
