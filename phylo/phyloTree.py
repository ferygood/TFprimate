from Bio import Phylo

# can also consider ETE toolkit

tree = Phylo.read("SpeciesTree.tr", "newick")
print(Phylo.draw_ascii(tree))
