# import os
# import gffutils
# from Bio import SeqIO

# # List of specific genes to extract
# genes_of_interest = ["dnaK", "gyrA", "gyrB", "ftsZ", "recA", "rpoB", "groEL"]

# # Directories
# gff_directory = '/Users/khandker_shahed/Documents/Work with Onu Vai/Paper/Piscirickettsia salmonis/Gff_files/input_files/'
# output_directory = '/Users/khandker_shahed/Documents/Work with Onu Vai/Paper/Piscirickettsia salmonis/output_fasta_files/'

# # Create the output directory if it does not exist
# if not os.path.exists(output_directory):
#     os.makedirs(output_directory)

# # Initialize a dictionary to hold gene sequences for each gene
# gene_sequences = {gene: [] for gene in genes_of_interest}

# # Iterate over each .gff file in the directory
# for gff_file in os.listdir(gff_directory):
#     if gff_file.endswith(".gff"):
#         print(f"Processing file: {gff_file}")
#         gff_path = os.path.join(gff_directory, gff_file)
        
#         # Create a database from the GFF file
#         db = gffutils.create_db(gff_path, dbfn='gff.db', force=True, keep_order=True, merge_strategy='merge')

#         # Extract gene features
#         gene_features = db.features_of_type('gene')
        
#         # Extract sequences for the genes of interest
#         for f in gene_features:
#             gene_id = f.attributes.get('ID', [None])[0]
#             if gene_id in genes_of_interest:
#                 seq = db.get_sequence(f.seqid, f.start, f.end, strand=f.strand)
#                 if seq:
#                     gene_sequences[gene_id].append(f">{gene_id}_{gff_file}\n{seq}\n")
#                     print(f"Added sequence for gene: {gene_id} from file: {gff_file}")

# # Write sequences to FASTA files
# for gene, sequences in gene_sequences.items():
#     output_file = os.path.join(output_directory, f"{gene}.fasta")
#     with open(output_file, 'w') as fasta_file:
#         fasta_file.writelines(sequences)
#     print(f"Saved {len(sequences)} sequences for {gene} to {output_file}")

# print("Processing completed.")

import os
import glob
from Bio import SeqIO

# Set the input directory containing the GFF files
input_dir = "/Users/khandker_shahed/Documents/Work with Onu Vai/Paper/Piscirickettsia salmonis/Gff_files/input_files/"

# Set the BED file containing the gene coordinates
bed_file = "/Users/khandker_shahed/Documents/Work with Onu Vai/Paper/Piscirickettsia salmonis/Gff_files/genes.bed"

# Set the output directory for the gene fasta files
output_dir = "/Users/khandker_shahed/Documents/Work with Onu Vai/Paper/Piscirickettsia salmonis/output_fasta_files/"

# Set the gene names
genes = ["dnaK", "gyrA", "gyrB", "ftsZ", "recA", "rpoB", "groEL"]

# Load the BED file
gene_coords = {}
with open(bed_file, 'r') as f:
    for line in f:
        fields = line.strip().split('\t')
        genome_id = fields[0]
        gene = fields[3]
        start = int(fields[1])
        end = int(fields[2])
        gene_coords.setdefault(genome_id, {})[gene] = (start, end)

# Initialize an empty dictionary to store sequences
sequences = {gene: [] for gene in genes}

# Loop through each GFF file
for file in glob.glob(os.path.join(input_dir, '*.gff')):
    genome_id = os.path.basename(file).split('.')[0]
    if genome_id not in gene_coords:
        print(f"Warning: No coordinates found for genome ID: {genome_id}. Skipping file: {file}")
        continue

    for gene in genes:
        if gene not in gene_coords[genome_id]:
            print(f"Warning: Gene {gene} not found in BED file for genome ID: {genome_id}. Skipping.")
            continue

        start, end = gene_coords[genome_id][gene]
        seq = ''
        with open(file, 'r') as f:
            for line in f:
                if line.startswith('#'):
                    continue
                fields = line.strip().split('\t')
                if len(fields) >= 9 and fields[2] == 'CDS':
                    try:
                        seq_info = fields[8]
                        if 'sequence=' in seq_info:
                            sequence = seq_info.split('sequence=')[1].split(';')[0]
                            if int(fields[3]) >= start and int(fields[4]) <= end:
                                seq += sequence
                        else:
                            print(f"Warning: 'sequence=' not found in line: {line}")
                    except IndexError as e:
                        print(f"IndexError: {e} in line: {line}")

        # Only write to file if sequence is not empty
        if seq:
            with open(os.path.join(output_dir, f"{gene}.fasta"), 'a') as f:
                f.write(f">{genome_id}_{gene}\n{seq}\n")
                print(f"Added sequence for gene: {gene} from file: {file}")

print("Processing completed.")


