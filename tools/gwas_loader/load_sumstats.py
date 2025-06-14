import gwaslab as gl
import sys

input_file = sys.argv[1]

sumstats = gl.Sumstats(input_file, fmt="plink2", sep=",")
sumstats.summary(outfile="summary.txt")
