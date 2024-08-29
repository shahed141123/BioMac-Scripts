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

# import os
# import glob
# from Bio import SeqIO

# # Set the input directory containing the GFF files
# input_dir = "/Users/khandker_shahed/Documents/Work with Onu Vai/Paper/Piscirickettsia salmonis/Gff_files/input_files/"

# # Set the BED file containing the gene coordinates
# bed_file = "/Users/khandker_shahed/Documents/Work with Onu Vai/Paper/Piscirickettsia salmonis/Gff_files/genes.bed"

# # Set the output directory for the gene fasta files
# output_dir = "/Users/khandker_shahed/Documents/Work with Onu Vai/Paper/Piscirickettsia salmonis/output_fasta_files/"

# # Set the gene names
# genes = ["dnaK", "gyrA", "gyrB", "ftsZ", "recA", "rpoB", "groEL"]

# # Load the BED file
# gene_coords = {}
# with open(bed_file, 'r') as f:
#     for line in f:
#         fields = line.strip().split('\t')
#         genome_id = fields[0]
#         gene = fields[3]
#         start = int(fields[1])
#         end = int(fields[2])
#         gene_coords.setdefault(genome_id, {})[gene] = (start, end)

# # Initialize an empty dictionary to store sequences
# sequences = {gene: [] for gene in genes}

# # Loop through each GFF file
# for file in glob.glob(os.path.join(input_dir, '*.gff')):
#     genome_id = os.path.basename(file).split('.')[0]
#     if genome_id not in gene_coords:
#         print(f"Warning: No coordinates found for genome ID: {genome_id}. Skipping file: {file}")
#         continue

#     for gene in genes:
#         if gene not in gene_coords[genome_id]:
#             print(f"Warning: Gene {gene} not found in BED file for genome ID: {genome_id}. Skipping.")
#             continue

#         start, end = gene_coords[genome_id][gene]
#         seq = ''
#         with open(file, 'r') as f:
#             for line in f:
#                 if line.startswith('#'):
#                     continue
#                 fields = line.strip().split('\t')
#                 if len(fields) >= 9 and fields[2] == 'CDS':
#                     try:
#                         seq_info = fields[8]
#                         if 'sequence=' in seq_info:
#                             sequence = seq_info.split('sequence=')[1].split(';')[0]
#                             if int(fields[3]) >= start and int(fields[4]) <= end:
#                                 seq += sequence
#                         else:
#                             print(f"Warning: 'sequence=' not found in line: {line}")
#                     except IndexError as e:
#                         print(f"IndexError: {e} in line: {line}")

#         # Only write to file if sequence is not empty
#         if seq:
#             with open(os.path.join(output_dir, f"{gene}.fasta"), 'a') as f:
#                 f.write(f">{genome_id}_{gene}\n{seq}\n")
#                 print(f"Added sequence for gene: {gene} from file: {file}")

# print("Processing completed.")


# from Bio import SeqIO
# from Bio.SeqRecord import SeqRecord
# import pandas as pd

# def extract_genes(fasta_file, gff_file, genes_of_interest):
#     # Read the GFF file into a DataFrame
#     gff_df = pd.read_csv(gff_file, sep='\t', comment='#', header=None)
#     gff_df.columns = ['seqid', 'source', 'feature', 'start', 'end', 'score', 'strand', 'phase', 'attributes']
#     gff_df = gff_df[gff_df['feature'] == 'gene']
    
#     # Filter for genes of interest
#     gff_df = gff_df[gff_df['attributes'].str.contains('|'.join(genes_of_interest))]
    
#     # Read the FASTA file
#     genome = SeqIO.read(fasta_file, 'fasta')
#     genome_seq = genome.seq

#     extracted_genes = {}
#     for _, row in gff_df.iterrows():
#         gene_name = row['attributes'].split(';')[0].split('=')[1]
#         if gene_name in genes_of_interest:
#             start = int(row['start']) - 1  # BED format is 0-based
#             end = int(row['end'])
#             seq = genome_seq[start:end]
#             if row['strand'] == '-':
#                 seq = seq.reverse_complement()
#             if gene_name not in extracted_genes:
#                 extracted_genes[gene_name] = []
#             extracted_genes[gene_name].append(SeqRecord(seq, id=f"{gene_name}_{row['seqid']}", description=""))

#     return extracted_genes

# # Example usage
# genes = ['dnaK', 'gyrA', 'gyrB', 'ftsZ', 'recA', 'rpoB', 'groEL']
# fasta_file = 'output_fasta/genome.fasta'
# gff_file = 'output_fasta/genome.gff'
# gene_sequences = extract_genes(fasta_file, gff_file, genes)

# # Save to separate FASTA files
# for gene_name, records in gene_sequences.items():
#     SeqIO.write(records, f'{gene_name}.fasta', 'fasta')


#!/bin/bash

# Directory containing GFF files
from Bio import SeqIO
import os
import glob

# List of gene names to extract
genes_to_extract = ['dnaK', 'gyrA', 'gyrB', 'ftsZ', 'recA', 'rpoB', 'groEL']

# Function to extract gene sequences directly from GFF files
def extract_genes_from_gff(gff_file_path, gene_names):
    gene_sequences = {gene: [] for gene in gene_names}
    fasta_sequences = None
    fasta_data = []
    in_fasta_section = False

    with open(gff_file_path, "r") as gff_file:
        print(f"Processing file: {gff_file_path}")
        
        for line in gff_file:
            if line.startswith("##FASTA"):
                in_fasta_section = True
                continue

            if in_fasta_section:
                fasta_data.append(line.strip())
            else:
                if line.startswith("#"):
                    continue
                parts = line.strip().split("\t")
                if len(parts) < 9:
                    continue
                if parts[2] == "gene":  # Look for gene features
                    attributes = {key_value.split("=")[0]: key_value.split("=")[1] for key_value in parts[8].split(";") if "=" in key_value}
                    gene_name = attributes.get("gene")
                    if gene_name in gene_names:
                        start = int(parts[3]) - 1  # Convert to 0-based index
                        end = int(parts[4])
                        strand = parts[6]

                        if fasta_sequences:  # Ensure sequence data is available
                            # Extract the sequence
                            gene_seq = fasta_sequences[start:end]
                            if strand == "-":
                                gene_seq = gene_seq.reverse_complement()

                            gene_sequences[gene_name].append(gene_seq)

    # Process FASTA section if present
    if fasta_data:
        fasta_sequences = "".join(fasta_data[1:])  # Remove header line and join sequence lines

    return gene_sequences

# Function to write extracted gene sequences to FASTA files
def write_gene_sequences_to_fasta(gene_sequences, output_dir):
    for gene, sequences in gene_sequences.items():
        output_file_path = os.path.join(output_dir, f"{gene}.fasta")
        with open(output_file_path, "w") as fasta_file:
            for i, seq in enumerate(sequences):
                fasta_file.write(f">{gene}_{i+1}\n{seq}\n")

# Paths to the uploaded GFF files using glob
gff_files = glob.glob('/mnt/f/Paper/BioMac-Scripts/input_files/*.gff')

# Directory to save the FASTA files
output_dir = "/mnt/f/Paper/BioMac-Scripts/output_fasta/"
os.makedirs(output_dir, exist_ok=True)

# Extract and write sequences for each GFF file
for gff_file in gff_files:
    gene_sequences = extract_genes_from_gff(gff_file, genes_to_extract)
    write_gene_sequences_to_fasta(gene_sequences, output_dir)

print(f"FASTA files have been created in {output_dir}.")
