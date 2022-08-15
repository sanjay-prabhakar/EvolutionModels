# Brown/blue is controlled by the B/b alleles, and dominant G turns on green if b.

class eye:
    def __init__(self,brown_1,brown_2,green_1,green_2):
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
        phenotype = eye(pair_1[0],pair_1[1],pair_2[0],pair_2[1]).colour()
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
            

from random import randint

def infer_genotype(colour):
    roll = randint(0,len(inferring[colour])-1)
    return inferring[colour][roll]



def gamete(eye):
    brown_roll = randint(1,2)
    if brown_roll == 1:
        brown_gam = eye.brown_1
    else:
        brown_gam = eye.brown_2
    green_roll = randint(1,2)
    if green_roll == 1:
        green_gam = eye.green_1
    else:
        green_gam = eye.green_2
    return [brown_gam,green_gam]


def offspring(sperm,egg):
    return eye(sperm[0],egg[0],sperm[1],egg[1])


if __name__ == '__main__':
    choose = input("Enter 1 to input phenotypes or 2 to input genotypes: ")
    if choose == "1":
        colour_1 = input("Please enter the first parent's eye colour: ")
        genotype_1 = infer_genotype(colour_1)
        print("The first parent has genotype {0} (chance of {1}%).".format(\
            genotype_1,round(chance[colour_1]*100,1)))
        print("Generating gamete...")
        eye_father = eye(genotype_1[0],genotype_1[1],genotype_1[2],genotype_1[3])
        sperm = gamete(eye_father)
        print("{0}{1}".format(sperm[0],sperm[1]))
        colour_2 = input("Please enter the second parent's eye colour: ")
        genotype_2 = infer_genotype(colour_2)
        print("The second parent has genotype {0} (chance of {1}%).".format(\
            genotype_2,round(chance[colour_2]*100,1)))
        print("Generating gamete...")
        eye_mother = eye(genotype_2[0],genotype_2[1],genotype_2[2],genotype_2[3])
        egg = gamete(eye_mother)
        print("{0}{1}".format(egg[0],egg[1]))
        print("Combining genes...")
        child = offspring(sperm,egg)
        print("The offspring has {0} eyes, with the genotype {1}.".format(child.colour(),\
                                                                          child.genotype()))
    elif choose == "2":
        print("First parent:")
        brown_1 = input("Please enter the first B/b allele: ")
        brown_2 = input("Please enter the second B/b allele: ")
        green_1 = input("Please enter the first G/g allele: ")
        green_2 = input("Please enter the second G/g allele: ")
        print("---")
        eye_father = eye(brown_1,brown_2,green_1,green_2)
        print("This genotype codes for {0} eyes.".format(eye_father.colour()))
        print("Generating gamete...")
        sperm = gamete(eye_father)
        print("{0}{1}".format(sperm[0],sperm[1]))
        print("Second parent:")
        brown_1 = input("Please enter the first B/b allele: ")
        brown_2 = input("Please enter the second B/b allele: ")
        green_1 = input("Please enter the first G/g allele: ")
        green_2 = input("Please enter the second G/g allele: ")
        print("---")
        eye_mother = eye(brown_1,brown_2,green_1,green_2)
        print("This genotype codes for {0} eyes.".format(eye_mother.colour()))
        print("Generating gamete...")
        egg = gamete(eye_mother)
        print("{0}{1}".format(egg[0],egg[1]))
        print("Combining genes...")
        child = offspring(sperm,egg)
        print("The offspring genotype is {0}{1}{2}{3}, expressed as {4}.".format(child.brown_1,\
                                                                                 child.brown_2,\
                                                                                 child.green_1,\
                                                                                 child.green_2,\
                                                                                 child.colour()))
   
