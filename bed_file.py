import os
import glob
import subprocess

# Set the input directory containing the 80 genome GFF files
input_dir = "/Users/khandker_shahed/Documents/Work with Onu Vai/Paper/Piscirickettsia salmonis/Gff_files/input_files/"

# Set the output file for the BED file
output_file = "/Users/khandker_shahed/Documents/Work with Onu Vai/Paper/Piscirickettsia salmonis/Gff_files/genes.bed"

# Set the gene names
genes = ['dnaK', 'gyrA', 'gyrB', 'ftsZ', 'recA', 'rpoB', 'groEL']

# Create a dictionary to store the gene coordinates
gene_coords = {}

# Loop through each GFF file
for file in glob.glob(os.path.join(input_dir, '*.gff')):
    # Extract the genome ID from the file name
    genome_id = os.path.basename(file).split('.')[0]

    # Loop through each gene
    for gene in genes:
        # Use subprocess to extract the coordinates of the gene from the GFF file
        command = ["grep", gene, file]
        try:
            output = subprocess.check_output(command, shell=False)
            output_decoded = output.decode()
            # Extract the coordinates from the output
            for line in output_decoded.split('\n'):
                if line:
                    fields = line.split('\t')
                    start = int(fields[3])
                    end = int(fields[4])
                    gene_coords.setdefault(genome_id, {})[gene] = (start, end)
        except subprocess.CalledProcessError:
            print(f"Skipping file {file} because grep command failed for gene {gene}")

# Create the BED file
with open(output_file, 'w') as f:
    for genome_id, gene_coords in gene_coords.items():
        for gene, (start, end) in gene_coords.items():
            f.write(f"{genome_id}\t{start}\t{end}\t{gene}\n")

