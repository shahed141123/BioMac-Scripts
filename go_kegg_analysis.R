# Load required libraries
library(AnnotationDbi)
# library(org.Hs.eg.db)
library(org.Mm.eg.db)
# library(org.Dr.eg.db)
library(clusterProfiler)
library(ggplot2)
library(scales)
library(KEGGREST) # For KEGG data access

# Define file paths
file_path <- '/Users/khandker_shahed/Documents/Work with Onu Vai/Paper/Go_enrich80gene/eggnog_output2.emapper.annotations'
go_output_file <- '/Users/khandker_shahed/Documents/Work with Onu Vai/Paper/Go_enrich80gene/go_id_counts.csv'
kegg_output_file <- '/Users/khandker_shahed/Documents/Work with Onu Vai/Paper/Go_enrich80gene/kegg_enrichment_results.csv'

# Load data
annotation_df <- read.csv(file_path, sep='\t', header=FALSE, comment.char='#')
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
# species_db <- org.Hs.eg.db
# species_code <- "hsa"
# species_db <- org.Dr.eg.db
# species_code <- "dre"
species_db <- org.Mm.eg.db
species_code <- "mmu"

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

# Convert enrichment results to a data frame
ego_df <- as.data.frame(ego)

# Convert GeneRatio from fraction string to numeric
# ego_df$GeneRatio <- sapply(strsplit(as.character(ego_df$GeneRatio), "/"), function(x) as.numeric(x[1]) / as.numeric(x[2]))
ego_df$GeneRatio <- sapply(strsplit(as.character(ego_df$GeneRatio), "/"), function(x) {
    if (length(x) == 2) {
        as.numeric(x[1]) / as.numeric(x[2])
    } else {
        NA
    }
})

# Filter to display only the top 20 significant GO terms
ego_df <- ego_df[order(ego_df$p.adjust), ][1:20, ]

# Create the dot plot for GO enrichment with GeneRatio formatted as a decimal fraction
ddotplot_go <- ggplot(ego_df, aes(x = GeneRatio, y = reorder(Description, GeneRatio), 
                                  size = Count, color = p.adjust)) +
    geom_point(alpha = 0.8) +
    scale_color_gradient(low = "purple", high = "green", name = "p.adjust") +
    scale_size_continuous(range = c(3, 10)) +
    scale_x_continuous(labels = scales::label_number()) + 
    labs(title = "GO Enrichment for Selected GO IDs",
         x = "Gene Ratio",
         y = NULL,
         size = "Count") +
    theme_minimal(base_size = 12) +
    theme(axis.text.y = element_text(size = 16, face = "bold", margin = margin(r = 10)),
          axis.title.x = element_text(size = 16, face = "bold"),
          plot.title = element_text(hjust = 1, size = 16, face = "bold"),
          legend.title = element_text(size = 14, face = "bold"),
          legend.text = element_text(size = 14))

# Save the GO dot plot
ggsave("/Users/khandker_shahed/Documents/Work with Onu Vai/Paper/Go_enrich80gene/go_enrichment_dotplot.png", 
       dotplot_go, width = 20, height = 15, dpi = 300)

# Perform KEGG pathway enrichment analysis
kegg_results <- enrichKEGG(gene = gene_list,
                           organism = species_code,
                           keyType = 'kegg',
                           pvalueCutoff = 0.05,
                           pAdjustMethod = "BH",
                           qvalueCutoff = 0.2,
                           universe = background_genes,
                           minGSSize = 10,
                           maxGSSize = 500)

# Convert KEGG results to a data frame
kegg_df <- as.data.frame(kegg_results)

# Convert GeneRatio from fraction string to numeric
kegg_df$GeneRatio <- sapply(strsplit(as.character(kegg_df$GeneRatio), "/"), function(x) {
    if (length(x) == 2) {
        as.numeric(x[1]) / as.numeric(x[2])
    } else {
        NA
    }
})

# Remove rows with NA or problematic values
kegg_df_clean <- kegg_df[!is.na(kegg_df$GeneRatio), ]

# Filter to display only the top 20 significant KEGG pathways
kegg_df_clean <- kegg_df_clean[order(kegg_df_clean$p.adjust), ][1:20, ]

# Create the dot plot for KEGG enrichment with GeneRatio formatted as a decimal fraction
dotplot_kegg <- ggplot(kegg_df_clean, aes(x = GeneRatio, y = reorder(Description, GeneRatio), 
                                          size = Count, color = p.adjust)) +
    geom_point(alpha = 0.6) +
    scale_color_gradient(low = "red", high = "blue", name = "p.adjust") +
    scale_size_continuous(range = c(3, 10)) +
    scale_x_continuous(labels = scales::label_number()) +
    labs(title = "KEGG Pathway Enrichment for Selected Genes",
         x = "Gene Ratio",
         y = NULL,
         size = "Count") +
    theme_minimal(base_size = 12) +
    theme(axis.text.y = element_text(size = 16, face = "bold", margin = margin(r = 10)),
          axis.title.x = element_text(size = 16, face = "bold"),
          plot.title = element_text(hjust = 1, size = 16, face = "bold"),
          legend.title = element_text(size = 14, face = "bold"),
          legend.text = element_text(size = 14))

# Save the KEGG dot plot
ggsave("/Users/khandker_shahed/Documents/Work with Onu Vai/Paper/Go_enrich80gene/kegg_enrichment_dotplot.png", 
       dotplot_kegg, width = 20, height = 15, dpi = 300)