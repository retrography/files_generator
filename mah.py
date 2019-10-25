#!/usr/bin/env python3

import sys

infile1 = sys.argv[1]
infile2 = sys.argv[2]
outdir = sys.argv[3]

txt1 = f.read(infile1)
txt2 = f.read(infile2)
out = [txt1]

slice_size = 5

out += [" ".join(met.split(" ")[5:])]
out += [" ".join(met.split(" ")[0:-5])]