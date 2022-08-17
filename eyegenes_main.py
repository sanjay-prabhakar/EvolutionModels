from eyegenes import EyeGenes, string_to_EyeGenes, Chromosome_to_EyeGenes, recombination_eye, reproduce_eye
from chromosomes import Gene, Chromosome, string_to_Chromosome, recombination, reproduce
from eyecolour import infer_genotype
import matplotlib.pyplot as plt

if __name__ == '__main__':
    n_brown = int(input("Enter the number of brown-eyed people in the founding population: "))
    n_green = int(input("Enter the number of green-eyed people in the founding population: "))
    n_blue = int(input("Enter the number of blue-eyed people in the founding population: "))
    founder_pop_size = n_brown + n_green + n_blue
    founders_input = {"brown": n_brown, "green": n_green, "blue": n_blue}
    founders_proportion = {}
    for colour in founders_input:
        founders_proportion[colour] = founders_input[colour] / founder_pop_size
    founders = []
    for colour in founders_input:
        for i in range(founders_input[colour]):
            genotype = infer_genotype(colour)
            founders.append(string_to_EyeGenes(genotype))
    fertility = int(input("Enter the number of offspring per couple: ")) # TODO: incorporate variable fertility by eye colour
    generations = int(input("To which generation would you like to evolve? The founding population is the 1st "
                            "generation. "))
    all_gens = {1: founders}
    for i in range(1, generations):
        new_gen = reproduce_eye(all_gens[i], fertility)
        all_gens[i+1] = new_gen
    all_numbers = {}
    for generation in all_gens:
        all_numbers[generation] = {"brown": 0, "green": 0, "blue": 0, "total": 0}
        for each in all_gens[generation]:
            all_numbers[generation][each.colour()] += 1
            all_numbers[generation]["total"] += 1
    all_props = {}
    for generation in all_gens:
        all_props[generation] = {"brown": all_numbers[generation]["brown"] / all_numbers[generation]["total"],
                                 "green": all_numbers[generation]["green"] / all_numbers[generation]["total"],
                                 "blue": all_numbers[generation]["blue"] / all_numbers[generation]["total"]}
    all_brown = []
    all_green = []
    all_blue = []
    all_totals = []
    for generation in all_gens:
        all_brown.append(all_numbers[generation]["brown"])
        all_green.append(all_numbers[generation]["green"])
        all_blue.append(all_numbers[generation]["blue"])
        all_totals.append(all_numbers[generation]["total"])
    #print(all_brown)
    #print(all_green)
    #print(all_blue)
    print(all_totals)
    generations = list(range(1, generations + 1))
    plt.plot(generations, all_brown, color = "brown")
    plt.plot(generations, all_green, color = "green")
    plt.plot(generations, all_blue, color = "blue")
    plt.title("Number of members of generations with each eye colour")
    plt.xlabel("Generation")
    plt.xticks(generations)
    plt.ylabel("Number")
    plt.show()



    '''
    offspring = reproduce_eye(founders, fertility)
    offspring_output = {"brown": 0, "green": 0, "blue": 0}
    for child in offspring:
        offspring_output[child.colour()] += 1
    offspring_pop_size = len(offspring)
    offspring_proportion = {}
    for colour in offspring_output:
        offspring_proportion[colour] = offspring_output[colour] / offspring_pop_size
    brown_rate = offspring_proportion["brown"]
    green_rate = offspring_proportion["green"]
    blue_rate = offspring_proportion["blue"]
    print("After one generation:")
    print(f"- the proportion of brown eyes has gone from {round(n_brown / founder_pop_size * 100, 1)}% to"
          f"{round(offspring_proportion['brown'] * 100, 1)}%")
    print(f"- the proportion of green eyes has gone from {round(n_green / founder_pop_size * 100, 1)}% to"
          f"{round(offspring_proportion['green'] * 100, 1)}%")
    print(f"- the proportion of blue eyes has gone from {round(n_blue / founder_pop_size * 100, 1)}% to"
          f"{round(offspring_proportion['blue'] * 100, 1)}%")
    '''
