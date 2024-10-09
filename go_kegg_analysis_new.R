# Install BiocManager if not already installed
# if (!requireNamespace("BiocManager", quietly = TRUE)) {
#   install.packages("BiocManager")
# }

# Install the Bioconductor packages (AnnotationDbi, org.Mm.eg.db, and clusterProfiler)
# BiocManager::install(c("AnnotationDbi", "org.Hs.eg.db", "org.Dr.eg.db", "org.Mm.eg.db", "clusterProfiler", "KEGGREST"))
# Install the CRAN packages (ggplot2 and scales)
# install.packages(c("ggplot2", "scales"))




# Load necessary libraries
library(AnnotationDbi)
library(org.Hs.eg.db)         # Mouse genome annotations
# library(org.Hs.eg.db)
# library(org.Dr.eg.db)
library(clusterProfiler)      # For enrichment analysis
library(ggplot2)               # For plotting
library(scales)                # For scales in plots
library(KEGGREST)              # For KEGG data access

# Function to perform GO enrichment analysis
perform_GO_enrichment <- function(gene_list, species_db, background_genes) {
  ego <- enrichGO(gene = gene_list,
                  OrgDb = species_db,
                  keyType = 'ENTREZID',
                  ont = "ALL",
                  pvalueCutoff = 0.05,
                  pAdjustMethod = "BH",
                  qvalueCutoff = 0.2,
                  universe = background_genes,
                  minGSSize = 10,
                  maxGSSize = 500,
                  readable = TRUE)
  return(ego)
}

# Function to perform KEGG enrichment analysis
perform_KEGG_enrichment <- function(gene_list, species_code, background_genes) {
  kegg_results <- enrichKEGG(gene = gene_list,
                             organism = species_code,
                             keyType = 'kegg',
                             pvalueCutoff = 0.05,
                             pAdjustMethod = "BH",
                             qvalueCutoff = 0.2,
                             universe = background_genes,
                             minGSSize = 10,
                             maxGSSize = 500)
  return(kegg_results)
}

# Function to process GeneRatio (convert fraction string to numeric)
convert_GeneRatio <- function(df) {
  df$GeneRatio <- sapply(strsplit(as.character(df$GeneRatio), "/"), function(x) {
    if (length(x) == 2) {
      as.numeric(x[1]) / as.numeric(x[2])
    } else {
      NA
    }
  })
  return(df)
}

# Function to create dot plot
create_dotplot <- function(df, title, output_file, color_low, color_high) {
  dotplot <- ggplot(df, aes(x = GeneRatio, y = reorder(Description, GeneRatio), 
                            size = Count, color = p.adjust)) +
    geom_point(alpha = 0.8) +
    scale_color_gradient(low = color_low, high = color_high, name = "p.adjust") +
    scale_size_continuous(range = c(3, 10)) +
    scale_x_continuous(labels = scales::label_number()) + 
    labs(title = title,
         x = "Gene Ratio",
         y = NULL,
         size = "Count") +
    theme_minimal(base_size = 12) +
    theme(axis.text.y = element_text(size = 16, face = "bold", margin = margin(r = 10)),
          axis.title.x = element_text(size = 16, face = "bold"),
          plot.title = element_text(hjust = 1, size = 16, face = "bold"),
          legend.title = element_text(size = 14, face = "bold"),
          legend.text = element_text(size = 14))
  
  ggsave(output_file, dotplot, width = 20, height = 15, dpi = 300)
}

# Load and clean data
file_path <- 'F:/Research/marinum/eggnog_output.emapper.annotations'
go_output_file <- 'F:/Research/marinum/go_id_counts.csv'
kegg_output_file <- 'F:/Research/marinum/kegg_enrichment_results.csv'

# Check if the input file exists before reading
if (!file.exists(file_path)) {
  stop("The file at path '", file_path, "' does not exist.")
}

# Load the annotation data
annotation_df <- read.csv(file_path, sep = '\t', header = FALSE, comment.char = '#')
colnames(annotation_df) <- c('query', 'seed_ortholog', 'evalue', 'score', 'eggNOG_OGs',
                              'max_annot_lvl', 'COG_category', 'Description', 'Preferred_name',
                              'GOs', 'EC', 'KEGG_ko', 'KEGG_Pathway', 'KEGG_Module',
                              'KEGG_Reaction', 'KEGG_rclass', 'BRITE', 'KEGG_TC', 'CAZy',
                              'BiGG_Reaction', 'PFAMs')

# Extract and clean GO IDs
go_ids <- unlist(strsplit(as.character(annotation_df$GOs[!is.na(annotation_df$GOs)]), split = ","))
go_ids <- go_ids[go_ids != "-"]
go_id_counts <- table(go_ids)
write.csv(go_id_counts, go_output_file)

# Choose species and load corresponding organism database
species_db <- org.Hs.eg.db
species_code <- "hsa"

# Retrieve genes associated with each GO term
valid_go_ids <- intersect(go_ids, keys(species_db, keytype = "GO"))
if (length(valid_go_ids) == 0) {
  stop("No valid GO IDs found.")
}

genes_associated <- do.call(rbind, lapply(valid_go_ids, function(go_id) {
  AnnotationDbi::select(species_db, keys = go_id, columns = c("SYMBOL", "ENTREZID"), keytype = "GO")
}))
gene_list <- unique(genes_associated$ENTREZID)

# Define the background gene set (all Entrez IDs in the database)
background_genes <- keys(species_db, keytype = "ENTREZID")

# Perform GO enrichment analysis
ego <- perform_GO_enrichment(gene_list, species_db, background_genes)

# Convert enrichment results to a data frame and process GeneRatio
ego_df <- as.data.frame(ego)
ego_df <- convert_GeneRatio(ego_df)

# Filter to display only the top 20 significant GO terms
ego_df <- ego_df[order(ego_df$p.adjust), ][1:20, ]

# Create the GO dot plot
go_dotplot_file <- "/F:/Research/marinum/go_enrichment_dotplot.png"
create_dotplot(ego_df, "GO Enrichment for Selected GO IDs", go_dotplot_file, "purple", "green")

# Perform KEGG pathway enrichment analysis
kegg_results <- perform_KEGG_enrichment(gene_list, species_code, background_genes)

# Convert KEGG results to a data frame and process GeneRatio
kegg_df <- as.data.frame(kegg_results)
kegg_df <- convert_GeneRatio(kegg_df)

# Remove rows with NA or problematic values
kegg_df_clean <- kegg_df[!is.na(kegg_df$GeneRatio), ]

# Filter to display only the top 20 significant KEGG pathways
kegg_df_clean <- kegg_df_clean[order(kegg_df_clean$p.adjust), ][1:20, ]

# Create the KEGG dot plot
kegg_dotplot_file <- "/F:/Research/marinum/kegg_enrichment_dotplot.png"
create_dotplot(kegg_df_clean, "KEGG Pathway Enrichment for Selected Genes", kegg_dotplot_file, "red", "blue")

# Save the KEGG enrichment results to file
write.csv(kegg_df_clean, kegg_output_file)
