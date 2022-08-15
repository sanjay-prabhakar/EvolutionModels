from random import randint

class gene:
    # The class expects two strings for the alleles, which are upper or lower case variants
    # of the same letter
    def __init__(self,allele_1,allele_2):
        self.allele_1 = allele_1
        self.allele_2 = allele_2


    def genotype_gene(self):
        return "{0}{1}".format(self.allele_1,self.allele_2)

    def phenotype_gene(self):
        if self.allele_1.isupper():
            return self.allele_1
        else:
            return self.allele_2

    def meiosis_gene(self):
        return [self.allele_1,self.allele_2][randint(0,1)]


def reproduce_gene(father,mother):
    return gene(father.meiosis(),mother.meiosis())


class chromosome:
    # The class expects a list of genes
    def __init__(self,genes):
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
        selection = randint(1,2)
        gamete = []
        for gene in self.genes:
            gamete.append([gene.allele_1,gene.allele_2][selection-1])
        return gamete


def recombination(father,mother):
    # The function takes two chromosomal pairs and performs meiosis with recombination
    num_genes = len(father.genes)
    print("The number of genes is {0}.".format(num_genes))
    crossover = randint(1,num_genes)
    # Genes are swapped after this locus
    print("The recombination crossover point is {0}.".format(crossover))
    sperm = father.meiosis()
    print("The sperm carries {0}.".format(sperm))
    egg = mother.meiosis()
    print("The egg carries {0}.".format(egg))
    recombined_1 = []
    recombined_2 = []
    for i in range(crossover):
        recombined_1.append(sperm[i])
        recombined_2.append(egg[i])
    for i in range(crossover,num_genes):
        recombined_1.append(egg[i])
        recombined_2.append(sperm[i])
    print("The recombined sequences are {0} and {1}.".format(recombined_1,recombined_2))
    new_genes = []
    for j in range(num_genes):
        new_genes.append(gene(recombined_1[j],recombined_2[j]))
    return chromosome(new_genes)


if __name__ == '__main__':
    chromosome_length = int(input("How many genes would you like in each chromosome? "))
    print("The father:")
    father_genes = []
    for i in range(chromosome_length):
        first_allele = input("The first allele of gene {0}: ".format(i+1))
        second_allele = input("The second allele of gene {0}: ".format(i+1))
        father_genes.append(gene(first_allele,second_allele))
    father = chromosome(father_genes)
    print("The mother:")
    mother_genes = []
    for i in range(chromosome_length):
        first_allele = input("The first allele of gene {0}: ".format(i+1))
        second_allele = input("The second allele of gene {0}: ".format(i+1))
        mother_genes.append(gene(first_allele,second_allele))
    mother = chromosome(mother_genes)
    child = recombination(father,mother)
    print("The father's genotype is {0}, the mother's genotype is {1}, and the child's genotype is {2}."\
      .format(father.genotype(),mother.genotype(),child.genotype()))
    print("The father's phenotype is {0}, the mother's phenotype is {1}, and the child's phenotype is {2}."\
      .format(father.phenotype(),mother.phenotype(),child.phenotype()))
        
        
        
    
    
