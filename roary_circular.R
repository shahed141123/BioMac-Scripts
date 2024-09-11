# Install ggtree if you don't have it
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install("ggtree")
install.packages("ggtree", force = TRUE)

# Load libraries
library(ggtree)
library(treeio)

# Load your phylogenetic tree (Newick format)
tree <- read.tree("/Users/khandker_shahed/Documents/vibrio_anguillarum/roary_output/core_gene_alignment.tree")

# Plot the circular phylogenetic tree
p <- ggtree(tree, layout = "circular")

# Customize and add more layers (like the presence/absence matrix)
# Assuming you have your Roary presence/absence matrix in a CSV format
gene_matrix <- read.csv("/Users/khandker_shahed/Documents/vibrio_anguillarum/roary_output/gene_presence_absence.csv", header = TRUE)

# You can map these matrix data to the tips or branches of the tree
# Custom code to add presence/absence info to the tree
# Install and load necessary packages
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("ggtree")
install.packages("treeio")

# Load libraries
library(ggtree)
library(treeio)
library(ggplot2)

# Load your phylogenetic tree (Newick format)
tree <- read.tree("/Users/khandker_shahed/Documents/vibrio_anguillarum/roary_output/core_gene_alignment.tree")

# Load presence/absence matrix
gene_matrix <- read.csv("/Users/khandker_shahed/Documents/vibrio_anguillarum/roary_output/gene_presence_absence.csv", header = TRUE)

# View the first few rows of the matrix to understand its structure
head(gene_matrix)

# Prepare the data: Assume 'Sample' column in gene_matrix matches tree tip labels
# Ensure that the presence/absence data aligns with the tree's tip labels
tree_data <- data.frame(tip = tree$tip.label)

# Check the structure of gene_matrix (assumed columns: Gene, Sample, Presence)
# You might need to adjust this part according to your actual data
if ("Sample" %in% colnames(gene_matrix) & "Presence" %in% colnames(gene_matrix)) {
    # Map presence/absence data to tree tip labels
    tree_data$presence <- ifelse(tree_data$tip %in% gene_matrix$Sample,
                                 gene_matrix$Presence[match(tree_data$tip, gene_matrix$Sample)],
                                 NA)
} else {
    stop("Expected columns 'Sample' and 'Presence' in the gene matrix.")
}

# Plot the circular phylo
