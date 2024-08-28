import pandas as pd
import gseapy as gp
import matplotlib.pyplot as plt
from Bio.KEGG import REST

# Define file paths
file_path = '/Users/khandker_shahed/Documents/Work with Onu Vai/Paper/Go_enrich80gene/eggnog_output2.emapper.annotations'
go_output_file = '/path/to/save/go_id_counts.csv'
kegg_output_file = '/path/to/save/kegg_enrichment_results.csv'

# Define column names based on the structure
column_names = [
    'query', 'seed_ortholog', 'evalue', 'score', 'eggNOG_OGs',
    'max_annot_lvl', 'COG_category', 'Description', 'Preferred_name',
    'GOs', 'EC', 'KEGG_ko', 'KEGG_Pathway', 'KEGG_Module',
    'KEGG_Reaction', 'KEGG_rclass', 'BRITE', 'KEGG_TC', 'CAZy',
    'BiGG_Reaction', 'PFAMs'
]

# Load the file and process GO IDs
def load_and_process_data(file_path):
    try:
        annotation_df = pd.read_csv(file_path, delimiter='\t', header=None, names=column_names, comment='#')
        if 'GOs' in annotation_df.columns:
            go_ids = annotation_df['GOs'].dropna().tolist()
            go_ids = [go for sublist in go_ids for go in sublist.split(',') if go and go != '-']
            go_id_counts = pd.Series(go_ids).value_counts()
            go_id_counts.to_csv(go_output_file, header=True)
            return go_ids
        else:
            print("Column 'GOs' not found in the file.")
            return None
    except pd.errors.ParserError as e:
        print(f"ParserError: {e}")
        return None
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Perform GO Enrichment Analysis
def perform_go_enrichment(go_ids):
    if go_ids:
        go_enrichment = gp.enrichr(
            gene_list=go_ids,
            gene_sets='GO_Biological_Process_2021',  # Or another relevant GO term set
            organism='Human',
            outdir=None  # Set to a path if you want to save the results
        )
        print("\nGO Enrichment Analysis Results:")
        print(go_enrichment.results.head())
    else:
        print("No GO IDs available for enrichment analysis.")

# Perform KEGG Pathway Enrichment Analysis
def perform_kegg_enrichment(go_ids):
    if go_ids:
        # Convert GO IDs to KEGG pathway IDs if needed
        # Here we'll assume go_ids are KEGG pathway IDs directly

        # Example pathway IDs, replace with actual KEGG IDs or conversion
        kegg_ids = [go for go in go_ids if go.startswith('KEGG:')]
        kegg_enrichment = gp.enrichr(
            gene_list=kegg_ids,
            gene_sets='KEGG_2021_Human',  # Or another relevant KEGG term set
            organism='Human',
            outdir=None  # Set to a path if you want to save the results
        )
        print("\nKEGG Pathway Enrichment Analysis Results:")
        print(kegg_enrichment.results.head())
    else:
        print("No KEGG pathway IDs available for enrichment analysis.")

# Example function to retrieve KEGG pathways (if required)
def retrieve_kegg_pathways():
    kegg_pathways = REST.kegg_list("pathway").read()
    print("\nKEGG Pathways:")
    print(kegg_pathways)

# Main execution
go_ids = load_and_process_data(file_path)
perform_go_enrichment(go_ids)
perform_kegg_enrichment(go_ids)
retrieve_kegg_pathways()
