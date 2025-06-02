# #!/usr/bin/env python3
# import sys
# import pandas as pd

# def main():
#     input_file = sys.argv[1]
#     threshold = float(sys.argv[2])
#     output_file = sys.argv[3]

#     # Load and filter
#     df = pd.read_csv(input_file, sep='\t')
#     if "p-value" not in df.columns:
#         raise ValueError("Input file must contain a 'p-value' column.")
#     filtered_df = df[df["p-value"] < threshold]

#     # Save output
#     filtered_df.to_csv(output_file, sep='\t', index=False)

# if __name__ == "__main__":
#     main()
# # Usage: python gwas_filter.py input_file.tsv threshold output_file.tsv




#!/usr/bin/env python3
import sys
import pandas as pd

def main():
    input_file = sys.argv[1]
    threshold = float(sys.argv[2])
    output_file = sys.argv[3]

    df = pd.read_csv(input_file, sep='\t')
    if "p-value" not in df.columns:
        raise ValueError("Input file must contain a 'p-value' column.")
    
    filtered_df = df[df["p-value"] < threshold]
    filtered_df.to_csv(output_file, sep='\t', index=False)

if __name__ == "__main__":
    main()












# <tool id="gwas_filter" name="GWAS Result Filter" version="1.0.0" python_template_version="3.5">
#     <description>Filter GWAS results based on p-value</description>

#     <!-- <command interpreter="python3"><![CDATA[
#          '$script' '$input_file' '$pval_threshold' '$output_file'
#     ]]></command> -->
#     <command interpreter="python3"><![CDATA[
#     '$script' '$input_file' '$pval_threshold' '$output_file'
#     ]]></command>


#     <inputs>
#         <param name="input_file" type="data" format="tabular" label="GWAS Results Table" />
#         <param name="pval_threshold" type="float" value="0.05" label="P-value threshold" />
#         <param name="script" type="hidden" value="gwas_filter.py" />
#     </inputs>

#     <outputs>
#     </outputs>        <data name="output_file" format="tabular" label="Filtered GWAS Results" />


#     <help><![CDATA[
# This tool filters a GWAS results table by a p-value threshold.
# Only SNPs with p-values below the threshold will be kept in the output.

# **Inputs:**
# - GWAS results table with at least two columns: "SNP" and "p-value"
# - User-defined threshold (default: 0.05)

# **Output:**
# - A filtered table containing only SNPs with p-values below the threshold.
#     ]]></help>
# </tool>











