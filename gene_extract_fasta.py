# import os
# import re
# from Bio import SeqIO

# # Directories
# genome_dir = "/Users/khandker_shahed/Documents/Work with Onu Vai/Piscirickettsia salmonis/gcs_files"
# output_dir = "/Users/khandker_shahed/Documents/Work with Onu Vai/Piscirickettsia salmonis/output_fasta"
# result_file = "/Users/khandker_shahed/Documents/Work with Onu Vai/Piscirickettsia salmonis/output_fasta/result.txt"

# # List of target genes
# target_genes = ["dnaK", "gyrA", "gyrB", "ftsZ", "recA", "rpoB", "groEL"]

# # Dictionary to store sequences for each gene
# gene_sequences = {gene: [] for gene in target_genes}
# missing_genes = {gene: [] for gene in target_genes}  # Track missing genes

# # Open result file for writing
# with open(result_file, "w") as result_f:
#     def log_message(message):
#         print(message)  # Print to console
#         result_f.write(message + "\n")  # Write to file

#     # Function to parse .fna files and extract target gene sequences
#     def extract_gene_sequences(file_path):
#         genome_id = os.path.basename(file_path).split(".")[0]  # Use filename as genome ID
#         found_genes = set()  # Track genes found in this genome
#         with open(file_path, "r") as handle:
#             for record in SeqIO.parse(handle, "fasta"):
#                 description = record.description
#                 sequence = str(record.seq)
                
#                 # Extract the accession ID from the description
#                 accession_match = re.search(r'lcl\|([^\s]+)', description)
#                 accession_id = accession_match.group(1) if accession_match else "Unknown"

#                 # Search for target genes using regex to match [gene=gene_name]
#                 for gene in target_genes:
#                     gene_pattern = re.compile(rf"\[gene={gene}\]", re.IGNORECASE)
#                     if gene_pattern.search(description):
#                         found_genes.add(gene)
#                         gene_sequences[gene].append(f">{accession_id}_{genome_id} {description}\n{sequence}")

#         # Check for missing genes in this genome
#         for gene in target_genes:
#             if gene not in found_genes:
#                 missing_genes[gene].append(genome_id)

#     # Iterate through all .fna files in the genome directory
#     for filename in os.listdir(genome_dir):
#         if filename.endswith(".fna"):
#             extract_gene_sequences(os.path.join(genome_dir, filename))

#     # Write output FASTA files for each gene
#     for gene, sequences in gene_sequences.items():
#         with open(os.path.join(output_dir, f"{gene}.fasta"), "w") as output_file:
#             output_file.write("\n".join(sequences))
#         log_message(f"FASTA file for {gene} written to {output_dir}/{gene}.fasta")

#     # Log missing genes
#     for gene, missing in missing_genes.items():
#         if missing:
#             log_message(f"Missing {gene} in genomes: {', '.join(missing)}")
#         else:
#             log_message(f"All genomes have {gene}.")

#     log_message("Gene sequences have been extracted and written to the output directory.")



# import os
# import re
# from Bio import SeqIO

# # Directories
# genome_dir = "/Users/khandker_shahed/Documents/Work with Onu Vai/Piscirickettsia salmonis/gcs_files"
# output_dir = "/Users/khandker_shahed/Documents/Work with Onu Vai/Piscirickettsia salmonis/output_fasta"
# result_file = "/Users/khandker_shahed/Documents/Work with Onu Vai/Piscirickettsia salmonis/output_fasta/result.txt"
# # List of target genes and corresponding descriptions
# target_genes = {
#     "dnaK": ["dnaK"],  # Keeping it simple for genes strictly named as is
#     "gyrA": ["gyrA", "DNA gyrase subunit A", "gyrase subunit A"],
#     "gyrB": ["gyrB", "DNA gyrase subunit B", "gyrase subunit B"],
#     "ftsZ": ["ftsZ", "cell division protein FtsZ"],
#     "recA": ["recA", "DNA recombination/repair protein RecA"],
#     "rpoB": ["rpoB"],  # Assuming this one is named consistently
#     "groEL": ["groEL"]  # Assuming this one is named consistently
# }

# # Dictionary to store sequences for each gene
# gene_sequences = {gene: [] for gene in target_genes}
# missing_genes = {gene: [] for gene in target_genes}  # Track missing genes

# with open(result_file, "w") as result_f:
#     def log_message(message):
#         print(message)  # Print to console
#         result_f.write(message + "\n")  # Write to file
# # Function to parse .fna files and extract target gene sequences
# def extract_gene_sequences(file_path):
#     genome_id = os.path.basename(file_path).split(".")[0]  # Use filename as genome ID
#     found_genes = set()  # Track genes found in this genome
#     with open(file_path, "r") as handle:
#         for record in SeqIO.parse(handle, "fasta"):
#             description = record.description
#             sequence = str(record.seq)
            
#             # Extract the accession ID from the description
#             accession_match = re.search(r'lcl\|([^\s]+)', description)
#             accession_id = accession_match.group(1) if accession_match else "Unknown"

#             # Search for target genes using regex to match gene names or descriptions
#             for gene, patterns in target_genes.items():
#                 for pattern in patterns:
#                     gene_pattern = re.compile(rf"\[gene={pattern}\]|\[protein={pattern}\]", re.IGNORECASE)
#                     if gene_pattern.search(description):
#                         found_genes.add(gene)
#                         gene_sequences[gene].append(f">{accession_id}_{genome_id} {description}\n{sequence}")
#                         break  # Stop searching once a match is found for this gene

#     # Check for missing genes in this genome
#     for gene in target_genes:
#         if gene not in found_genes:
#             missing_genes[gene].append(genome_id)

# # Iterate through all .fna files in the genome directory
# for filename in os.listdir(genome_dir):
#     if filename.endswith(".fna"):
#         extract_gene_sequences(os.path.join(genome_dir, filename))

# # Write output FASTA files for each gene
# for gene, sequences in gene_sequences.items():
#     with open(os.path.join(output_dir, f"{gene}.fasta"), "w") as output_file:
#         output_file.write("\n".join(sequences))

# # Log missing genes
# # for gene, missing in missing_genes.items():
# #     if missing:
# #         print(f"Missing {gene} in genomes: {', '.join(missing)}")
# #     else:
# #         print(f"All genomes have {gene}.")

# # print("Gene sequences have been extracted and written to the output directory.")
# #     # Log missing genes
#     for gene, missing in missing_genes.items():
#         if missing:
#             log_message(f"Missing {gene} in genomes: {', '.join(missing)}")
#         else:
#             log_message(f"All genomes have {gene}.")

#     log_message("Gene sequences have been extracted and written to the output directory.")

# iimport os
# import re
# from Bio import SeqIO

# # Directories
# genome_dir = "/Users/khandker_shahed/Documents/Work with Onu Vai/Piscirickettsia salmonis/gcs_files"
# output_dir = "/Users/khandker_shahed/Documents/Work with Onu Vai/Piscirickettsia salmonis/output_fasta"
# result_file = "/Users/khandker_shahed/Documents/Work with Onu Vai/Piscirickettsia salmonis/output_fasta/result.txt"

# # Define the gene search terms (with variations) for each target gene
# target_genes = {
#     "dnaK": ["dnaK"],
#     "gyrA": ["gyrA", "gyrase subunit A"],
#     "gyrB": ["gyrB", "gyrase subunit B"],
#     "ftsZ": ["ftsZ", "cell division protein FtsZ"],
#     "recA": ["recA", "DNA recombination/repair protein RecA"],
#     "rpoB": ["rpoB"],
#     "groEL": ["groEL"]
# }

# # Dictionary to store sequences for each gene
# gene_sequences = {gene: [] for gene in target_genes}
# missing_genes = {gene: [] for gene in target_genes}  # Track missing genes

# Function to parse .fna files and extract target gene sequences
# def extract_gene_sequences(file_path):
#     genome_id = os.path.basename(file_path).split(".")[0]  # Use filename as genome ID
#     found_genes = set()  # Track genes found in this genome
#     with open(file_path, "r") as handle:
#         for record in SeqIO.parse(handle, "fasta"):
#             description = record.description
#             sequence = str(record.seq)

#             # Extract the accession ID from the description
#             prefix = "Accession ID : "
#             accession_match = re.search(r'lcl\|([^\s]+)', description)
#             accession_id = accession_match.group(1) if accession_match else "Unknown"

#             # Search for target genes using regex to match variations
#             for gene, patterns in target_genes.items():
#                 # Create a case-sensitive pattern for the exact gene name
#                 exact_pattern = re.compile(r'\b' + re.escape(gene) + r'\b')
#                 # Search for exact gene name matches
#                 if exact_pattern.search(description):
#                     found_genes.add(gene)
#                     gene_sequences[gene].append(f">{genome_id}\n{sequence}")
#                 # If the gene is not found, check for other variations
#                 elif gene not in found_genes:
#                     for pattern in patterns:
#                         if re.search(pattern, description, re.IGNORECASE):
#                             if pattern not in [gene for gene in target_genes.values()]:
#                                 found_genes.add(gene)
#                                 gene_sequences[gene].append(f">{genome_id}\n{sequence}")

#     # Check for missing genes in this genome
#     for gene in target_genes:
#         if gene not in found_genes:
#             missing_genes[gene].append(genome_id)

# # Iterate through all .fna files in the genome directory
# for filename in os.listdir(genome_dir):
#     if filename.endswith(".fna"):
#         extract_gene_sequences(os.path.join(genome_dir, filename))

# # Write output FASTA files for each gene
# for gene, sequences in gene_sequences.items():
#     with open(os.path.join(output_dir, f"{gene}.fasta"), "w") as output_file:
#         output_file.write("\n".join(sequences))

# # Log missing genes to result.txt
# with open(result_file, "w") as result_f:
#     for gene, missing in missing_genes.items():
#         if missing:
#             result_f.write(f"Missing {gene} in genomes: {', '.join(missing)}\n")
#         else:
#             result_f.write(f"All genomes have {gene}.\n")

# print("Gene sequences have been extracted and written to the output directory.")
# print(f"Results have been logged to {result_file}.")


import os
import re
from Bio import SeqIO

# Directories
genome_dir = "/Users/khandker_shahed/Documents/vibrio_anguillarum/gcs_files/"
output_dir = "/Users/khandker_shahed/Documents/vibrio_anguillarum/output_fasta"
result_file = "/Users/khandker_shahed/Documents/vibrio_anguillarum/output_fasta/result.txt"

# Define the gene search terms (with variations) for each target gene
target_genes = {
    # "dnaK": ["dnaK"],
    # "gyrA": ["gyrA", "gyrase subunit A"],
    "lacZ": ["lacZ", "Beta-galactosidase"],
    "rpoN": ["rpoN", "RNA polymerase sigma-54 factor"],
    "ftsZ": ["ftsZ", "cell division protein FtsZ"],
    "feoB": ["feoB", "Ferrous iron transport protein B"],
    "nadC": ["nadC", "Nicotinate-nucleotide pyrophosphorylase (carboxylating)"]
}

# Dictionary to store sequences for each gene
gene_sequences = {gene: [] for gene in target_genes}
missing_genes = {gene: [] for gene in target_genes}  # Track missing genes

# Function to parse .fna files and extract target gene sequences
def extract_gene_sequences(file_path):
    genome_id = os.path.basename(file_path).split(".")[0]  # Use filename as genome ID
    found_genes = set()  # Track genes found in this genome
    with open(file_path, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            description = record.description
            sequence = str(record.seq)

            # Extract the accession ID from the description
            prefix = "Accession ID : "
            accession_match = re.search(r'lcl\|([^\s]+)', description)
            accession_id = accession_match.group(1) if accession_match else "Unknown"

            # First perform case-sensitive exact match
            for gene in target_genes.keys():
                exact_pattern = re.compile(r'\b' + re.escape(gene) + r'\b')
                if exact_pattern.search(description):
                    if gene not in found_genes:
                        found_genes.add(gene)
                        gene_sequences[gene].append(f">{genome_id}\n{sequence}")
                    break  # Skip further searches for this genome if gene found

            # If the exact match was not found, check for variations
            for gene, patterns in target_genes.items():
                if gene not in found_genes:  # Only check if the gene was not already found
                    for pattern in patterns:
                        if re.search(pattern, description, re.IGNORECASE):
                            found_genes.add(gene)
                            gene_sequences[gene].append(f">{genome_id}\n{sequence}")
                            break  # Move to the next gene after finding a match

    # Check for missing genes in this genome
    for gene in target_genes:
        if gene not in found_genes:
            missing_genes[gene].append(genome_id)

# Iterate through all .fna files in the genome directory
for filename in os.listdir(genome_dir):
    if filename.endswith(".fna"):
        extract_gene_sequences(os.path.join(genome_dir, filename))

# Write output FASTA files for each gene
for gene, sequences in gene_sequences.items():
    with open(os.path.join(output_dir, f"{gene}.fasta"), "w") as output_file:
        output_file.write("\n".join(sequences))

# Log missing genes to result.txt
with open(result_file, "w") as result_f:
    for gene, missing in missing_genes.items():
        if missing:
            result_f.write(f"Missing {gene} in genomes: {', '.join(missing)}\n")
        else:
            result_f.write(f"All genomes have {gene}.\n")

print("Gene sequences have been extracted and written to the output directory.")
print(f"Results have been logged to {result_file}.")
