import gwaslab as gl
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Input .csv file (PLINK2 format)')
    parser.add_argument('--output', required=True, help='Output summary text')
    args = parser.parse_args()

    # Load sumstats
    sumstats = gl.Sumstats(args.input, fmt="plink2", sep=",")

    # Write a summary of the dataframe
    with open(args.output, 'w') as out:
        out.write("=== gwaslab Loaded Summary ===\n")
        out.write(f"File: {args.input}\n")
        out.write(f"Shape: {sumstats.df.shape}\n")
        out.write("Columns:\n")
        out.write(str(sumstats.df.dtypes))
        out.write("\n\nPreview:\n")
        out.write(str(sumstats.df.head(10)))

if __name__ == "__main__":
    main()
