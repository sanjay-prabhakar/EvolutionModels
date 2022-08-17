from chromosomes import Gene, Chromosome, string_to_Chromosome, recombination, reproduce

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


def Chromosome_to_EyeGenes(chromosome):
    return EyeGenes(chromosome.get_genes())


def recombination_eye(father, mother):
    return EyeGenes(recombination(father, mother).get_genes())


def reproduce_eye(pop, fertility):
    offspring_chromosomes = reproduce(pop, fertility)
    offspring_eyes = []
    for child in offspring_chromosomes:
        offspring_eyes.append(Chromosome_to_EyeGenes(child))
    return offspring_eyes


def string_to_EyeGenes(string):
    genes = []
    for i in range(0, len(string), 2):
        genes.append(Gene(string[i], string[i+1]))
    return EyeGenes(genes)

'''
eye_1 = string_to_Chromosome("BBGG")
eye_2 = string_to_Chromosome("bbgg")
eye_3 = string_to_Chromosome("BbgG")
eye_4 = string_to_Chromosome("BBgg")
pop = [eye_1, eye_2, eye_3, eye_4]
children = reproduce(pop,2)
for child in children:
    print(child.genotype())
'''