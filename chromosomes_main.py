from chromosomes import Gene, reproduce_gene, Chromosome, recombination

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
