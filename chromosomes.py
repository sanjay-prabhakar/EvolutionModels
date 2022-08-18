from random import randint, shuffle
from numpy.random import normal

class Gene:
    # The class expects two strings for the alleles, which are upper or lower case variants
    # of the same letter
    def __init__(self, allele_1, allele_2):
        self.allele_1 = allele_1
        self.allele_2 = allele_2

    def __add__(self, other):
        return Chromosome([self, other])

    def genotype_gene(self):
        return f"{self.allele_1}{self.allele_2}"

    def phenotype_gene(self):
        if self.allele_1.isupper():
            return self.allele_1
        else:
            return self.allele_2

    def meiosis_gene(self):
        return [self.allele_1, self.allele_2][randint(0, 1)]


def string_to_Gene(string):
    return Gene(string[0],string[1])


def reproduce_gene(father, mother):
    return Gene(father.meiosis(), mother.meiosis())


class Chromosome:
    # The class expects a list of genes
    def __init__(self, genes):
        self.genes = genes

    def __add__(self, other):
        return Chromosome(self.genes + other.genes)

    def loci(self):
        return len(self.genes)

    def get_genes(self):
        return self.genes

    def genotype(self):
        result = []
        for gene in self.genes:
            result.append(gene.allele_1)
            result.append(gene.allele_2)
        return ''.join(result)

    def phenotype(self):
        result = []
        for gene in self.genes:
            result.append(gene.phenotype_gene())
        return ''.join(result)

    def meiosis(self):
        selection = randint(1, 2)
        gamete = []
        for gene in self.genes:
            gamete.append([gene.allele_1, gene.allele_2][selection - 1])
        return gamete


def string_to_Chromosome(string):
    genes = []
    for i in range(0, len(string), 2):
        genes.append(Gene(string[i], string[i+1]))
    return Chromosome(genes)


def recombination(father, mother):
    # The function takes two chromosomal pairs and performs meiosis with recombination
    num_genes = len(father.genes)
    #print(f"The number of genes is {num_genes}.")
    crossover = randint(1, num_genes)
    # Genes are swapped after this locus
    #print(f"The recombination crossover point is {crossover}.")
    sperm = father.meiosis()
    #print(f"The sperm carries {sperm}.")
    egg = mother.meiosis()
    #print(f"The egg carries {egg}.")
    recombined_1 = []
    recombined_2 = []
    for i in range(crossover):
        recombined_1.append(sperm[i])
        recombined_2.append(egg[i])
    for i in range(crossover, num_genes):
        recombined_1.append(egg[i])
        recombined_2.append(sperm[i])
    #print(f"The recombined sequences are {recombined_1} and {recombined_2}.")
    new_genes = []
    for j in range(num_genes):
        new_genes.append(Gene(recombined_1[j], recombined_2[j]))
    return type(father)(new_genes)


def reproduce(pop, fertility):
    # randomly pairs members (= Chromosomes) of a population; each pair has n=fertilty offspring
    shuffle(pop)
    offspring = []
    for i in range(len(pop)-1, 2):
        num_offspring = round(normal(fertility, 1))
        for j in range(num_offspring):
            offspring.append(recombination(pop[i], pop[i+1]))
    return offspring
