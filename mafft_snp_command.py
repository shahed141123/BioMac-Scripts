for file in "/Users/khandker_shahed/Documents/Work with Onu Vai/Piscirickettsia salmonis/output_fasta/*.fasta"; 
do mafft --auto "$file" > "/Users/khandker_shahed/Documents/Work with Onu Vai/Piscirickettsia salmonis/output_fasta/aligned/${file%.fasta}_aligned.fasta"; done

for file in /Users/khandker_shahed/Documents/Work\ with\ Onu\ Vai/Piscirickettsia\ salmonis/output_fasta/*.fasta; do mafft --auto "$file" > /Users/khandker_shahed/Documents/Work\ with\ Onu\ Vai/Piscirickettsia\ salmonis/output_fasta/aligned/$(basename "${file%.fasta}_aligned.fasta"); done


for file in /Users/khandker_shahed/Documents/Work\ with\ Onu\ Vai/Piscirickettsia\ salmonis/output_fasta/aligned/*.fasta; do python msa2snp/msa2snp.py "$file" > "/Users/khandker_shahed/Documents/Work\ with\ Onu\ Vai/Piscirickettsia\ salmonis/output_fasta/aligned/snp/${file%.fasta}_snp.txt"; done


for file in *.fasta; do python msa2snp/msa2snp.py "$file" > "snp/${file%.fasta}_snp.txt"; done

for file in /Users/khandker_shahed/Documents/vibrio_anguillarum/output_fasta2/*.fasta; do mafft --auto "$file" > /Users/khandker_shahed/Documents/vibrio_anguillarum/output_fasta2/aligned/$(basename "${file%.fasta}_aligned.fasta"); done

for file in /Users/khandker_shahed/Documents/vibrio_anguillarum/output_fasta2/aligned/*.fasta; do python msa2snp.py "$file" > "${file%.fasta}_snp.txt"; done

for file in /Users/khandker_shahed/Documents/vibrio_anguillarum/output_fasta2/aligned/*.fasta; do python msa2snp.py "$file" > "${file%.fasta}_snp.txt"; done

do mafft --auto "$file" > "/Users/khandker_shahed/Documents/Work with Onu Vai/Piscirickettsia salmonis/output_fasta/aligned/${file%.fasta}_aligned.fasta"; done

mafft --auto hcp2.fasta > hcp2_aligned.fasta

pyani anim -i gca_files/ -o ani_results/
pyani anim -i gca_files -o ani_results
pyani -i gca_files/ -o pyani_output/ -m ANIm -g

roary_plots.py /corynebacterium_glutamicum/roary_output/core_gene_alignment.tree /corynebacterium_glutamicum/roary_output/gene_presence_absence.csv
python Roary_Heaps_Law.py /mnt/f/vibrio_anguillarum/roary_output/gene_presence_absence.Rtab 100

ls -d -1 /mnt/f/corynebacterium_glutamicum/gca_files/*.fna > /mnt/f/corynebacterium_glutamicum/input.txt

ggcaller --refs "/mnt/f/corynebacterium_glutamicum/input.txt" --out /mnt/f/corynebacterium_glutamicum/ggcaller_output

abricate --db vfdb --quiet *.fna > /mnt/f/corynebacterium_glutamicum/results_vfdb.tab

abricate --db vfdb --quiet gca_files/*.fna > /mnt/f/corynebacterium_glutamicum/abricate/results_vfdb.tab
abricate --db ncbi --quiet gca_files/*.fna > /mnt/f/corynebacterium_glutamicum/abricate/results_ncbi.tab


