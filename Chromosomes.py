from random import randint


class Gene:
    # The class expects two strings for the alleles, which are upper or lower case variants
    # of the same letter
    def __init__(self, allele_1, allele_2):
        self.allele_1 = allele_1
        self.allele_2 = allele_2

    def genotype_gene(self):
        return "{0}{1}".format(self.allele_1, self.allele_2)

    def phenotype_gene(self):
        if self.allele_1.isupper():
            return self.allele_1
        else:
            return self.allele_2

    def meiosis_gene(self):
        return [self.allele_1, self.allele_2][randint(0, 1)]


def reproduce_gene(father, mother):
    return Gene(father.meiosis(), mother.meiosis())


class Chromosome:
    # The class expects a list of genes
    def __init__(self, genes):
        self.genes = genes

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


def recombination(father, mother):
    # The function takes two chromosomal pairs and performs meiosis with recombination
    num_genes = len(father.genes)
    print(f"The number of genes is {num_genes}.")
    crossover = randint(1, num_genes)
    # Genes are swapped after this locus
    print(f"The recombination crossover point is {crossover}.")
    sperm = father.meiosis()
    print(f"The sperm carries {sperm}.")
    egg = mother.meiosis()
    print(f"The egg carries {egg}.")
    recombined_1 = []
    recombined_2 = []
    for i in range(crossover):
        recombined_1.append(sperm[i])
        recombined_2.append(egg[i])
    for i in range(crossover, num_genes):
        recombined_1.append(egg[i])
        recombined_2.append(sperm[i])
    print(f"The recombined sequences are {recombined_1} and {recombined_2}.")
    new_genes = []
    for j in range(num_genes):
        new_genes.append(Gene(recombined_1[j], recombined_2[j]))
    return Chromosome(new_genes)


if __name__ == '__main__':
    chromosome_length = int(input("How many genes would you like in each chromosome? "))
    print("The father:")
    father_genes = []
    for i in range(chromosome_length):
        first_allele = input(f"The first allele of gene {i + 1}: ")
        second_allele = input(f"The second allele of gene {i + 1}: ")
        father_genes.append(Gene(first_allele, second_allele))
    father = Chromosome(father_genes)
    print("The mother:")
    mother_genes = []
    for i in range(chromosome_length):
        first_allele = input(f"The first allele of gene {i + 1}: ")
        second_allele = input(f"The second allele of gene {i + 1}: ")
        mother_genes.append(Gene(first_allele, second_allele))
    mother = Chromosome(mother_genes)
    child = recombination(father, mother)
    print(f"The father's genotype is {father.genotype()}, the mother's genotype is {mother.genotype()}, \
and the child's genotype is {child.genotype()}.")
    print(f"The father's phenotype is {father.phenotype()}, the mother's phenotype is {mother.phenotype()}, \
and the child's phenotype is {child.phenotype()}.")
