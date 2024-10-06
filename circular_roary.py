from ete3 import Tree, TreeStyle

# Load the tree from Newick file

tree = Tree("/mnt/f/Research/corynebacterium_glutamicum_old/roary_output/core_gene_alignment.tree")

# Create a TreeStyle object for a circular tree
ts = TreeStyle()
ts.mode = "c"
ts.show_leaf_name = True  # To display genome names
ts.arc_start = -180  # Start of the circular plot
ts.arc_span = 360    # Full circle

# Render the tree and save to a file
tree.render("/mnt/f/Research/corynebacterium_glutamicum_old/roary_output/circular_tree.png", tree_style=ts)

