# Brown/blue is controlled by the B/b alleles, and dominant G turns on green if b.
from random import randint


class Eye:
    def __init__(self, brown_1, brown_2, green_1, green_2):
        self.brown_1 = brown_1
        self.brown_2 = brown_2
        self.green_1 = green_1
        self.green_2 = green_2

    def colour(self):
        if self.brown_1 == "B" or self.brown_2 == "B":
            return "brown"
        elif self.green_1 == "G" or self.green_2 == "G":
            return "green"
        else:
            return "blue"

    def genotype(self):
        return self.brown_1 + self.brown_2 + self.green_1 + self.green_2


expression = {}
brown_genes = ["BB", "Bb", "bb"]
green_genes = ["GG", "Gg", "gg"]
for pair_1 in brown_genes:
    for pair_2 in green_genes:
        genotype = pair_1 + pair_2
        phenotype = Eye(pair_1[0], pair_1[1], pair_2[0], pair_2[1]).colour()
        expression[genotype] = phenotype
inferring = {}
for colour in ["brown", "green", "blue"]:
    inferring[colour] = []
    for genotype in expression:
        if expression[genotype] == colour:
            inferring[colour].append(genotype)
chance = {}
for colour in inferring:
    chance[colour] = 1 / len(inferring[colour])


def infer_genotype(colour):
    roll = randint(0, len(inferring[colour]) - 1)
    return inferring[colour][roll]


def gamete(eye):
    brown_roll = randint(1, 2)
    if brown_roll == 1:
        brown_gam = eye.brown_1
    else:
        brown_gam = eye.brown_2
    green_roll = randint(1, 2)
    if green_roll == 1:
        green_gam = eye.green_1
    else:
        green_gam = eye.green_2
    return [brown_gam, green_gam]


def offspring(sperm, egg):
    return Eye(sperm[0], egg[0], sperm[1], egg[1])


if __name__ == '__main__':
    choose = input("Enter 1 to input phenotypes or 2 to input genotypes: ")
    if choose == "1":
        colour_1 = input("Please enter the first parent's eye colour: ")
        genotype_1 = infer_genotype(colour_1)
        print(f"The first parent has genotype {genotype_1} (chance of {round(chance[colour_1] * 100, 1)}%).")
        print("Generating gamete...")
        eye_father = Eye(genotype_1[0], genotype_1[1], genotype_1[2], genotype_1[3])
        sperm = gamete(eye_father)
        print(f"{sperm[0]}{sperm[1]}")
        colour_2 = input("Please enter the second parent's eye colour: ")
        genotype_2 = infer_genotype(colour_2)
        print(f"The second parent has genotype {genotype_2} (chance of {round(chance[colour_2] * 100, 1)}%).")
        print("Generating gamete...")
        eye_mother = Eye(genotype_2[0], genotype_2[1], genotype_2[2], genotype_2[3])
        egg = gamete(eye_mother)
        print(f"{egg[0]}{egg[1]}")
        print("Combining genes...")
        child = offspring(sperm, egg)
        print(f"The offspring has {child.colour()} eyes, with the genotype {child.genotype()}.")
    elif choose == "2":
        print("First parent:")
        brown_1 = input("Please enter the first B/b allele: ")
        brown_2 = input("Please enter the second B/b allele: ")
        green_1 = input("Please enter the first G/g allele: ")
        green_2 = input("Please enter the second G/g allele: ")
        print("---")
        eye_father = Eye(brown_1, brown_2, green_1, green_2)
        print(f"This genotype codes for {eye_father.colour()} eyes.")
        print("Generating gamete...")
        sperm = gamete(eye_father)
        print(f"{sperm[0]}{sperm[1]}")
        print("Second parent:")
        brown_1 = input("Please enter the first B/b allele: ")
        brown_2 = input("Please enter the second B/b allele: ")
        green_1 = input("Please enter the first G/g allele: ")
        green_2 = input("Please enter the second G/g allele: ")
        print("---")
        eye_mother = Eye(brown_1, brown_2, green_1, green_2)
        print(f"This genotype codes for {eye_mother.colour()} eyes.")
        print("Generating gamete...")
        egg = gamete(eye_mother)
        print(f"{egg[0]}{egg[1]}")
        print("Combining genes...")
        child = offspring(sperm, egg)
        print(
            f"The offspring genotype is {child.brown_1}{child.brown_2}{child.green_1}{child.green_2}, "
            f"expressed as {child.colour()}.")
