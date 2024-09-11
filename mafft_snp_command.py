for file in "/Users/khandker_shahed/Documents/Work with Onu Vai/Piscirickettsia salmonis/output_fasta/*.fasta"; 
do mafft --auto "$file" > "/Users/khandker_shahed/Documents/Work with Onu Vai/Piscirickettsia salmonis/output_fasta/aligned/${file%.fasta}_aligned.fasta"; done

for file in /Users/khandker_shahed/Documents/Work\ with\ Onu\ Vai/Piscirickettsia\ salmonis/output_fasta/*.fasta; do mafft --auto "$file" > /Users/khandker_shahed/Documents/Work\ with\ Onu\ Vai/Piscirickettsia\ salmonis/output_fasta/aligned/$(basename "${file%.fasta}_aligned.fasta"); done


for file in /Users/khandker_shahed/Documents/Work\ with\ Onu\ Vai/Piscirickettsia\ salmonis/output_fasta/aligned/*.fasta; do python msa2snp/msa2snp.py "$file" > "/Users/khandker_shahed/Documents/Work\ with\ Onu\ Vai/Piscirickettsia\ salmonis/output_fasta/aligned/snp/${file%.fasta}_snp.txt"; done


for file in *.fasta; do python msa2snp/msa2snp.py "$file" > "snp/${file%.fasta}_snp.txt"; done

for file in /Users/khandker_shahed/Documents/vibrio_anguillarum/output_fasta2/*.fasta; do mafft --auto "$file" > /Users/khandker_shahed/Documents/vibrio_anguillarum/output_fasta2/aligned/$(basename "${file%.fasta}_aligned.fasta"); done

for file in /Users/khandker_shahed/Documents/vibrio_anguillarum/output_fasta2/aligned/*.fasta; do python msa2snp.py "$file" > "${file%.fasta}_snp.txt"; done

for file in /Users/khandker_shahed/Documents/vibrio_anguillarum/output_fasta2/aligned/*.fasta; do python msa2snp.py "$file" > "${file%.fasta}_snp.txt"; done

