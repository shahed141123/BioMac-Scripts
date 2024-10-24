
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Your DataFrame creation code...
data = {
    "Assembly Number": [
        "GCA_000010225.1", "GCA_000011325.1", "GCA_013014885.1", "GCA_013046805.1",
        "GCA_001447865.2", "GCA_001518935.2", "GCA_001643035.1", "GCA_001683115.1",
        "GCA_001687645.1", "GCA_017579845.1", "GCA_018286655.1", "GCA_018884245.1",
        "GCA_001936195.1", "GCA_019504365.1", "GCA_019551735.1", "GCA_000196335.1",
        "GCA_002163915.1", "GCA_002220135.1", "GCA_002243555.1", "GCA_002277975.1",
        "GCA_002355675.1", "GCA_027569975.1", "GCA_002847405.1", "GCA_002847425.1",
        "GCA_029674605.1", "GCA_000382905.1", "GCA_000404145.1", "GCA_000404185.1",
        "GCA_000445015.1", "GCA_000742715.1", "GCA_000742735.1", "GCA_007430945.1",
        "GCA_007431185.1", "GCA_007833315.1", "GCA_007833335.1", "GCA_000828015.1"
    ],
    "Number of Genes": [
        3238,3099,3163,3208,3121,3062,3203,3086,3075,2844,3232,3109,3165,2894,2913,3138,3121,3086,3222,2712,3093,3053,3139,3169,3067,2992,3101,3103,2945,2932,2901,2954,2956,2938,2940,2984
    ],
    "Number of BCG per Genome": [
        25,23, 23, 26, 23, 23, 26, 23, 23, 15, 25, 23, 23, 23, 23, 23, 22, 23, 26, 14, 23, 23, 23, 23, 23, 23, 25, 25, 23, 23, 23, 23, 23, 23, 23, 28 
    ],
    # "Biosynthetic": [
    #     5, 4, 4, 5, 4, 4, 5, 4, 4, 3, 5, 4, 4, 4, 4, 4, 4, 4, 5, 2,
    #     4, 4, 4, 4, 4, 4, 4, 5, 5, 4, 4, 4, 4, 4, 4, 6
    # ],
    
    # "Biosynthetic Additional": [
    #     20, 19, 19, 21, 19, 19, 21, 19, 19, 12, 20, 19, 19, 19, 19, 19,
    #     18, 19, 21, 12, 19, 19, 19, 19, 19, 19, 19, 20, 20, 19, 19, 19,
    #     19, 19, 19, 22
    # ]
}


df = pd.DataFrame(data)
# Calculate Pearson Correlation
correlation = df[['Number of Genes', 'Number of BCG per Genome']].corr(method='pearson')
print("Pearson Correlation Coefficient:")
pearson_corr_value = correlation.iloc[0, 1]
print(correlation)

# Plot the Data
# plt.figure(figsize=(10, 6))
# sns.scatterplot(data=df, x='Number of Genes', y='Number of BCG per Genome')
# sns.regplot(data=df, x='Number of Genes', y='Number of BCG per Genome', scatter=False, color='red')

# plt.title('Scatter Plot of Number of Genes vs. Number of BCG per Genome')
# plt.xlabel('Number of Genes')
# plt.ylabel('Number of BCG per Genome')
# plt.grid()


# biosynthetic

# df = pd.DataFrame(data)
# # Calculate Pearson Correlation
# correlation = df[['Biosynthetic', 'Biosynthetic Additional']].corr(method='pearson')
# print("Pearson Correlation Coefficient:")
# print(correlation)

# # Plot the Data
# plt.figure(figsize=(10, 6))
# sns.scatterplot(data=df, x='Biosynthetic', y='Biosynthetic Additional')
# sns.regplot(data=df, x='Biosynthetic', y='Biosynthetic Additional', scatter=False, color='red')

# plt.title('Scatter Plot of Biosynthetic vs. Biosynthetic Additional')
# plt.xlabel('Biosynthetic')
# plt.ylabel('Biosynthetic Additional')
# plt.grid()

# Save the plot as an image
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Number of Genes', y='Number of BCG per Genome')
sns.regplot(data=df, x='Number of Genes', y='Number of BCG per Genome', scatter=False, color='red')

# Show Pearson Correlation Coefficient on the plot
# plt.text(3000, 15, f'Pearson Correlation: {pearson_corr_value:.2f}', fontsize=12, color='black', fontstyle='bold')

# plt.gca().text(0.95, 0.05, f'Pearson Correlation: {pearson_corr_value:.2f}' , transform=plt.gca().transAxes,
#                 fontsize=10, verticalalignment='top', horizontalalignment='right',
#                 bbox=dict(facecolor='white', alpha=0.5))
# x coordinate =0.95 , y coordinate =0.97
plt.gcf().text(0.95, 0.97, f'Pearson Correlation: {pearson_corr_value:.2f}', 
               fontsize=12, verticalalignment='top', horizontalalignment='right',
               bbox=dict(facecolor='white', alpha=0.5))
plt.title('Scatter Plot of Number of Genes vs. Number of BCG per Genome')
plt.xlabel('Number of Genes')
plt.ylabel('Number of BCG per Genome')
plt.grid()

# Save the plot as an image
plt.savefig('/mnt/f/Research/corynebacterium_glutamicum_old/manuscript/biosynthetic_vs_biosynthetic_additional.png')