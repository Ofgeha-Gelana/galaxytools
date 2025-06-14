import gwaslab as gl
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sys

# Load the input file path from arguments
sumstats_path = sys.argv[1]
out_prefix = sys.argv[2]

# Load summary statistics
sumstats = gl.Sumstats(sumstats_path, fmt="plink2", sep=",")

# Create a basic plot (you can expand this later)
sns.histplot(sumstats.df['P'], bins=100)
plt.title("P-value Distribution")
plt.xlabel("P-value")
plt.ylabel("Frequency")
plt.savefig(f"{out_prefix}_pval_hist.png")
