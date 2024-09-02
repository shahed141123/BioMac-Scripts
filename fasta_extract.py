from Bio import SeqIO

input_file = "/Users/khandker_shahed/Documents/Work with Onu Vai/fasta_extract/contigs.fasta"
output_file = "/Users/khandker_shahed/Documents/Work with Onu Vai/fasta_extract/filtered_sequences2.fasta"
length_threshold = 200

# Use a list to collect records that meet the criteria
filtered_records = []

# Parse the sequences in the input file
try:
    for record in SeqIO.parse(input_file, "fasta"):
        # Print the length and actual sequence for debugging
        seq_length = len(record.seq)
        print(f"Processing sequence {record.id} with length {seq_length}")
        print(f"Sequence content (first 50 chars): {record.seq[:50]}...")  # Print the first 50 characters for preview

        # Verify the length calculation
        if seq_length != len(record.seq):
            print(f"Warning: Length mismatch for {record.id}. Expected {seq_length}, got {len(record.seq)}")

        # Collect records longer than the threshold
        if seq_length > length_threshold:
            filtered_records.append(record)
        else:
            print(f"Skipping sequence {record.id} because its length ({seq_length}) is not greater than {length_threshold}")
except FileNotFoundError:
    print(f"Error: The file {input_file} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

# Write all filtered records to the output file at once
try:
    with open(output_file, "w") as outfile:
        SeqIO.write(filtered_records, outfile, "fasta")
    print(f"Filtering complete. {len(filtered_records)} sequences written to {output_file}.")
except Exception as e:
    print(f"An error occurred while writing to the output file: {e}")
