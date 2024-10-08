import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend
import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt

# Define the file path
# file_path = '/Users/khandker_shahed/Documents/Work with Onu Vai/Paper/Go_enrich80gene/eggnog_output2.emapper.annotations'
file_path = '/mnt/f/Research/marinum/go_kegg_analysis/eggnog_output.emapper.annotations'

# Define column names based on the structure
column_names = [
    'query', 'seed_ortholog', 'evalue', 'score', 'eggNOG_OGs',
    'max_annot_lvl', 'COG_category', 'Description', 'Preferred_name',
    'GOs', 'EC', 'KEGG_ko', 'KEGG_Pathway', 'KEGG_Module',
    'KEGG_Reaction', 'KEGG_rclass', 'BRITE', 'KEGG_TC', 'CAZy',
    'BiGG_Reaction', 'PFAMs'
]

try:
    # Load the file, specifying the column names and skipping metadata lines
    annotation_df = pd.read_csv(file_path, delimiter='\t', header=None, names=column_names, comment='#')

    # Print the first few rows of the dataframe to verify
    print("Data Preview:")
    print(annotation_df.head())

    # Extract GO IDs from the 'GOs' column
    if 'GOs' in annotation_df.columns:
        # Flatten and clean the GO IDs list
        go_ids = annotation_df['GOs'].dropna().tolist()
        go_ids = [go for sublist in go_ids for go in sublist.split(',') if go and go != '-']  # Remove placeholders

        # Count occurrences of each GO ID
        go_id_counts = pd.Series(go_ids).value_counts()

        # Display the top 10 GO IDs by count
        print("\nTop 10 GO IDs:")
        print(go_id_counts.head(10))

        # Define a minimum count threshold
        min_count = 100

        # Filter GO IDs that occur at least `min_count` times
        filtered_go_ids = go_id_counts[go_id_counts >= min_count]
        print(f"\nFiltered GO IDs (occurs at least {min_count} times):")
        print(filtered_go_ids)

        # Save the GO ID counts to a CSV file
        go_id_counts.to_csv('/mnt/f/Research/marinum/go_kegg_analysis/go_id_counts.csv', header=True)
        print("\nGO ID counts have been saved to 'go_id_counts.csv'.")

        # Plot the top 20 GO IDs
        top_20_go_ids = go_id_counts.head(20)
        plt.figure(figsize=(10, 8))
        top_20_go_ids.plot(kind='barh')
        plt.xlabel('Count')
        plt.ylabel('GO ID')
        plt.title('Top 20 GO IDs by Count')
        plt.gca().invert_yaxis()  # Highest counts at the top
        plt.show()

        # Explore a specific GO ID
        # specific_go_id = 'GO:0008150'
        # if specific_go_id in go_id_counts.index:
        #     print(f"\n{specific_go_id} appears {go_id_counts[specific_go_id]} times")
        # else:
        #     print(f"\n{specific_go_id} is not in the data.")

        # Clean data further
        go_ids_cleaned = [go.strip() for go in go_ids if go and go != '-']
        go_id_counts_cleaned = pd.Series(go_ids_cleaned).value_counts()
        print("\nCleaned GO ID Counts:")
        print(go_id_counts_cleaned)

    else:
        print("Column 'GOs' not found in the file.")

except pd.errors.ParserError as e:
    print(f"ParserError: {e}")
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
