import pandas as pd

# Load the tab-delimited file
df = pd.read_csv('/Users/khandker_shahed/Documents/vibrio_anguillarum/results_vfdb.tab', delimiter='\t')

# Save as CSV
df.to_csv('/Users/khandker_shahed/Documents/vibrio_anguillarum/results_vfdb.csv', index=False)
