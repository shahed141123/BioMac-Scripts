# import pandas as pd

# # Path to the gene_presence_absence.csv file
# file_path = '/Users/khandker_shahed/Documents/vibrio_anguillarum/roary_output/gene_presence_absence.csv'

# # Load the CSV file
# gene_data = pd.read_csv(file_path)

# # Extract genome columns (assuming genome-specific data starts at the 13th column)
# genome_columns = gene_data.columns[13:]  # Adjust based on the actual column structure

# # Find genes present in all genomes (i.e., no NaN values across the genome columns)
# core_genes = gene_data.dropna(subset=genome_columns)

# # Extract the core gene names
# core_gene_list = core_genes['Gene'].tolist()

# # Optionally, save the core genes to a file
# output_file = '/Users/khandker_shahed/Documents/vibrio_anguillarum/core_genes_list.txt'
# with open(output_file, 'w') as f:
#     for gene in core_gene_list:
#         f.write(f"{gene}\n")

# print(f"Total core genes found: {len(core_gene_list)}")
# print(f"Core genes saved to {output_file}")

import pandas as pd

# Path to the gene_presence_absence.csv file
file_path = '/Users/khandker_shahed/Documents/vibrio_anguillarum/roary_output/gene_presence_absence.csv'

# Load the CSV file
gene_data = pd.read_csv(file_path)

# Extract genome columns (assuming genome-specific data starts at the 13th column)
genome_columns = gene_data.columns[13:]

# Find genes present in all genomes (i.e., no NaN values across the genome columns)
core_genes = gene_data.dropna(subset=genome_columns)

# Extract the gene names and their corresponding full annotations
core_genes_info = core_genes[['Gene', 'Annotation']]

# Optionally, save the core genes with annotations to a file
output_file = '/Users/khandker_shahed/Documents/vibrio_anguillarum/core_genes_list.txt'
core_genes_info.to_csv(output_file, sep='\t', index=False)

print(f"Total core genes found: {len(core_genes_info)}")
print(f"Core genes with annotations saved to {output_file}")
