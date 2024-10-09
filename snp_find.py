
# import re

# file_path = '/Users/khandker_shahed/Documents/Work with Onu Vai/Piscirickettsia salmonis/output_fasta/aligned/snp/ftsZ_aligned_snp.txt'
# output_path = '/Users/khandker_shahed/Documents/Work with Onu Vai/Piscirickettsia salmonis/output_fasta/aligned/snp/snp_table/ftsZ_aligned_snp.txt'
# # Read the file
# with open(file_path, 'r') as file:
#     lines = file.readlines()

# # Initialize SNP dictionary
# snps = {}

# # Process each line to identify SNPs
# for line in lines[1:]:  # Skip the header line
#     parts = line.strip().split()
#     position = int(parts[0])
#     nucleotides = parts[1:]

#     # Check for SNPs with '/'
#     for idx, nucleotide in enumerate(nucleotides):
#         if '/' in nucleotide:
#             # Extract SNP description and previous nucleotide
#             snp_description = nucleotide
#             prev_nucleotide = nucleotides[idx - 1] if idx > 0 else 'N/A'
            
#             # Record SNP with the previous nucleotide
#             if position in snps:
#                 snps[position].add((prev_nucleotide, snp_description))
#             else:
#                 snps[position] = {(prev_nucleotide, snp_description)}

# # Print the SNP table
# print("SNP Table for dnaK Gene")
# snp_output = []
# for position, snp_set in sorted(snps.items()):
#     for prev_nuc, snp_desc in snp_set:
#         formatted_snp = f"{position} {prev_nuc} > {snp_desc}"
#         snp_output.append(formatted_snp)

# # Print and save the SNP table
# with open(output_path, 'w') as out_file:
#     out_file.write("SNP Table for dnaK Gene\n")
#     for line in snp_output:
#         print(line)
#         out_file.write(f"{line}\n")


import os
import glob

# Define paths
input_directory = '/mnt/f/marinum/gcs_files/output_fasta/aligned/'
output_directory = '/mnt/f/marinum/gcs_files/output_fasta/snp/'
# input_directory = '/Users/khandker_shahed/Documents/vibrio_anguillarum/output_fasta2/aligned/'
# output_directory = '/Users/khandker_shahed/Documents/vibrio_anguillarum/output_fasta2/snp/'

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Get all .txt files in the input directory
input_files = glob.glob(os.path.join(input_directory, '*.txt'))

for file_path in input_files:
    file_name = os.path.basename(file_path)
    output_path = os.path.join(output_directory, file_name)
    
    # Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Initialize SNP dictionary
    snps = {}

    # Process each line to identify SNPs
    for line in lines[1:]:  # Skip the header line
        parts = line.strip().split()
        position = int(parts[0])
        nucleotides = parts[1:]

        # Check for SNPs with '/'
        for idx, nucleotide in enumerate(nucleotides):
            if '/' in nucleotide:
                # Extract SNP description and previous nucleotide
                snp_description = nucleotide
                prev_nucleotide = nucleotides[idx - 1] if idx > 0 else 'N/A'
                
                # Record SNP with the previous nucleotide
                if position in snps:
                    snps[position].add((prev_nucleotide, snp_description))
                else:
                    snps[position] = {(prev_nucleotide, snp_description)}

    # Print the SNP table
    snp_output = []
    for position, snp_set in sorted(snps.items()):
        for prev_nuc, snp_desc in snp_set:
            formatted_snp = f"{position} {prev_nuc} > {snp_desc}"
            snp_output.append(formatted_snp)

    # Write the SNP table to the output file
    with open(output_path, 'w') as out_file:
        out_file.write(f"SNP Table for {file_name.split('_')[0]} Gene\n")
        for line in snp_output:
            out_file.write(f"{line}\n")

    # Print progress
    print(f"Processed {file_name} and saved SNP table to {output_path}")
