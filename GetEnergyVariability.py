#! /usr/bin/env python

# Copyright (c) 2017 Martin Rosellen

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
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm

def main(argv):
    parser = argparse.ArgumentParser(description='Outputs the variance and range [abs(max-min)] of energy values. Lines'
                                                 ' starting with \'+\' are especially high values (range > 15,18,20).')
    parser.add_argument('energies', help='file with energy values generated by ExtractMMPBSATotals.py')
    parser.add_argument('output', help='file to write to')
    parser.add_argument('n_traj', help='number of frames from each trajectory that got used in the energy calculation')
    args = parser.parse_args()

    n = int(args.n_traj)

    with open(args.energies, 'r') as f:
        # start from second line (omit header)
        content = f.readlines()[1:]
        content = [float(item) for item in content]

        var = []
        rng = []
        out = ""
        for i in range(0, len(content), n):
            variance = np.var(content[i:i+n])
            var.append(variance)
            r = np.ptp(content[i:i+n])
            rng.append(r)
            if r > 15:
                out += "+"
            if r > 18:
                out += "+"
            if r > 20:
                out += "+"
            out += "\t\ttrajectory " + str((i+n)/n) + " \tvar: " + str(round(variance,2)) + " \trange: " + str(round(r,2))
            out += "\n"
        out += "--------\n"
        out += "variance mean: " + str(round(np.mean(var),2))
        out += "\n"
        out += "range mean: " + str(round(np.mean(rng),2))

        print out
        print "WARNING: Numbers of trajectories not necessarily the same as in file names. Please make sure that " \
              "trajectories are used in ascending order by mmpbsa to ensure correct numbering."

        ga
        # the histogram of the data
        n, bins, patches = plt.hist(var, 30, normed=1, facecolor='green', alpha=0.75)

        # best fit of data
        (mu, sigma) = norm.fit(var)

        # add a 'best fit' line
        y = mlab.normpdf(bins, mu, sigma)
        l = plt.plot(bins, y, 'r--', linewidth=1)

        plt.grid(True)

        plt.savefig('variance_histogram.png')

    with open(args.output, 'w') as o:
        o.write(out)

if __name__ == "__main__":
    main(sys.argv)