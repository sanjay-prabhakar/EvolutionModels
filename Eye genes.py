from Chromosomes import Gene, Chromosome

class EyeGenes(Chromosome):
    def __init__(self, genes):
        super().__init__(genes)

    def colour(self):
        brown_genes = self.genes[0]
        green_genes = self.genes[1]
        if "B" in brown_genes.genotype_gene():
            return "brown"
        elif "G" in green_genes.genotype_gene():
            return "green"
        else:
            return "blue"


brown_gene = Gene("B", "b")
green_gene = Gene("G", "G")
eye_genes = EyeGenes([brown_gene, green_gene])
print(eye_genes.colour())