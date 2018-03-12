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


import sys
import argparse
import re

def main(argv):
    parser = argparse.ArgumentParser(description='Exchange the residue numbers in the given file with the ones from the '
                                                 'reference mapping. The regex further restricts replacing positions')
    parser.add_argument('file', help='data where residue numbers should be exchanged')
    parser.add_argument('mapping', help='residue number mapping file')
    parser.add_argument('precedent', help='term that specifies what comes before a residue number')
    parser.add_argument('subsequent', help='term that specifies what comes after a residue number')
    args = parser.parse_args()

    mapping = args.mapping

    file = args.file

    precedent = args.precedent
    subsequent = args.subsequent

    mappings = {}
    with open(mapping, 'r') as f:
        content = f.readlines()
        for line in content:
            if len(line) > 1:
                temp = line.split()
                mappings[precedent + temp[0] + subsequent] = precedent + temp[1] + subsequent

    out = ""
    with open(file, 'r') as g:
        content = g.readlines()
        for line in content:
            for res, map in mappings.items():
                if res in line:
                    out += line.replace(res, map)


if __name__ == "__main__":
    main(sys.argv)
