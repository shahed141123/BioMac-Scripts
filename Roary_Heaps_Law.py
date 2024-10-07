import numpy as np
import random
import sys
import matplotlib.pyplot as plt  # Uncommented for plotting
from scipy.optimize import curve_fit

def heaps_law(x, k, alpha):
    return k * x**(alpha)

if len(sys.argv) < 3:
    print("Usage: python script.py <data_file> <iterations>")
    sys.exit(1)

print("Loading data!")

# Transpose gene presence-absence matrix
r = []

for h, line in enumerate(open(sys.argv[1])):
    tmp = line.strip().split('\t')[1:]
    if h == 0: 
        continue
    tmp = [int(x) for x in tmp]
    r.append(tmp)

r = np.array(r).T
num_genomes, num_genes = r.shape

print("Number of genomes: ", num_genomes, "\nNumber of genes: ", num_genes, "\n")

print("Calculating Heap's Law!")

# Estimate parameters of Heap's Law
x, y = [], []

for iteration in range(int(sys.argv[2])):
    print('Iteration: ', iteration + 1, end="\r")
    result = np.zeros(num_genes)
    c = list(range(num_genomes))
    random.shuffle(c)
    for h, i in enumerate(c):
        x.append(h + 1)
        result += r[i]
        y.append(np.count_nonzero(result))

# Fit the data using curve_fit
initial_guess = [1, 0.5]  # Initial guess for k and alpha
pars, cov = curve_fit(f=heaps_law, xdata=x, ydata=y, p0=initial_guess, bounds=(0, np.inf))
k, alpha = pars

print("\nk = ", k, "\ngamma = ", alpha, "\n")

# Plotting the results
plt.scatter(x, y, label='Data')
plt.plot(x, heaps_law(np.array(x), k, alpha), color='red', label='Fitted curve')
plt.xlabel('Number of genomes sampled')
plt.ylabel('Number of unique genes')
plt.legend()
plt.title("Heap's Law")

pangenome_status = "open" if alpha > 0 else "closed"
# Adding text annotations
# f'Number of genomes: {num_genomes}\n'
#              f'Number of genes: {num_genes}\n'
#              f'Iterations: {sys.argv[2]}\n'
text_str = (f'k = {k}\n'
             f'gamma = {alpha}\n'
             f'Pangenome is {"open" if alpha > 0 else "closed"}')

# Place the text in the bottom right corner
plt.gca().text(0.95, 0.05, text_str, transform=plt.gca().transAxes,
                fontsize=10, verticalalignment='bottom', horizontalalignment='right',
                bbox=dict(facecolor='white', alpha=0.5))

# Highlight the pangenome status with color


plt.show()

