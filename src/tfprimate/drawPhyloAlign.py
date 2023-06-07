from Bio import SeqIO
import json
from Bio import Phylo


def drawPhyloAlign():
	Names = []
	for record in SeqIO.parse("ENSG00000288631_codon.fa", "fasta"):
		Names.append(record.description)
	tree = Phylo.read("SpeciesTree.tr", "newick")

	for clade in tree.get_terminals():
		if clade.name in Names:
			clade.color = 'magenta'
	tree.root.color = "gray"
	phylo_tree = Phylo.draw(tree)
	return(phylo_tree)	
	
	
if __name__ == "__main__":
    drawPhyloAlign()