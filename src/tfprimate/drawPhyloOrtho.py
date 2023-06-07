import json
from Bio import Phylo


def drawPhyloOrtho():
	f = open('test1.json')
	data = json.load(f)
	Names = []
	for key, value in data.items():
		if value != "NA":
			Names.append(key)
	del Names[0:2]
	Names.pop()
	
	tree = Phylo.read("SpeciesTree_oldNames.tr", "newick")
	for clade in tree.get_terminals():
		if clade.name in Names:
			clade.color = 'cyan'
	tree.root.color = "gray"
	phylo_tree = Phylo.draw(tree)

	return(phylo_tree)
	
	
if __name__ == "__main__":
    drawPhyloOrtho()