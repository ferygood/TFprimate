from Bio import Phylo

# can also consider ETE toolkit

tree = Phylo.read("exampleTree", "newick")
print(Phylo.draw_ascii(tree))
