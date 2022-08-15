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

