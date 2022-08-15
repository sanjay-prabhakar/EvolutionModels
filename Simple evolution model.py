from random import randint

def mutate(offspring):
    new = []
    for baby in offspring:
        roll = randint(1,6)
        if roll == 1:
            new.append(baby - 1)
        elif roll == 6:
            new.append(baby + 1)
        else:
            new.append(baby)
    return new


def reproduce(parents,printing):
    offspring = mutate(parents) + mutate(parents)
    if printing == True:
        print("The offspring are {0}".format(offspring))
    return offspring
    

def select(pop,printing):
    predator = randint(2,6)
    if printing == True:
        print("The predator number is {0}".format(predator))
    survivors = []
    for animal in pop:
        if animal % predator != 0:
            survivors.append(animal)
    if printing == True:
        if len(survivors) == 0:
            print("The population has gone extinct.")
        else:
            print("The survivors are {0}".format(survivors))
    return survivors


def evolve(pop,printing):
    return select(reproduce(pop,printing),printing)


def ordinal(n):
    if n == 1:
        return "st"
    elif n == 2:
        return "nd"
    elif n == 3:
        return "rd"
    else:
        return "th"


def gen_n(pop,n,printing):
    # Generates the nth generation, where pop is the 1st generation
    if printing == True:
        print("The starting generation is {0}".format(pop))
    if n == 1:
        if printing == True:
            print("This is the 1st generation.")
        return pop
    result = pop
    for i in range(1,n):
        result = evolve(result,printing)
    if printing == True:
        max = len(pop) * 2 ** (n - 1)
        print("This is the {0}{1} generation, of size {2} of a maximum of {3}, which is {4}%.".format(n,ordinal(n),len(result),max,(len(result)/max) * 100))
    return result


def is_prime(n):
    if n < 3:
        return False
    for i in range(2,int(n/2)):
        if (n%i) == 0:
            return False
    return True

def vulnerability(n):
    result = 0
    for i in range(2,7):
        if n % i == 0:
            result += 1
    return result


def pop_stats(pop):
    print("The population size is {0}".format(len(pop)))
    unique = []
    for animal in pop:
        if animal not in unique:
            unique.append(animal)
    unique.sort()
    print("...")
    print("The extant characteristics are {0}".format(unique))
    distribution = {}
    for char in unique:
        distribution[char] = pop.count(char)
    print("...")
    print("The number of animals with each characteristic is:")
    print(distribution)
    proportion = {}
    for char in distribution:
        proportion[char] = round((distribution[char] / len(pop)) * 100, 2)
    print("...")
    print("The percentage of animals with each characteristic is:")
    print(proportion)
    primes_prop = 0
    for char in unique:
        if is_prime(char):
            primes_prop += proportion[char]
    print("...")
    print("The proportion of animals with a prime number characteristic is {0}%.".format(round(primes_prop,2)))
    vuln_index = 0
    for char in unique:
        vuln_index += vulnerability(char) * proportion[char] / 100
    print("...")
    print("The vulnerability index is {0}, compared to a maximum of 5.".format(round(vuln_index,2)))
    return distribution


def ave_growth(initial,final,n):
    return (final / initial) ** (1/(n-1)) - 1


def analyse_n(pop,n):
    print("Analysis of the {0}{1} generation given the founding population {2}:".format(n,ordinal(n),pop))
    result = pop_stats(gen_n(pop,n,False))
    pop_size = 0
    for char in result:
        pop_size += result[char]
    growth = ave_growth(len(pop),pop_size,n)
    print("The average growth rate is {0}% per generation, compared to a maximum of 100%.".format(round(growth * 100,2)))


def statistical_n(pop,n,runs):
    print("Statistical analysis of the {0}{1} generation given the founding population {2} from {3} simulations:".format(n,ordinal(n),pop,runs))
    result = []
    for i in range(runs):
        result += gen_n(pop,n,False)
    distribution = pop_stats(result)
    growth = ave_growth(len(pop)*runs,len(result),n)
    print("...")
    print("The average growth rate is {0}% per generation, compared to a maximum of 100%.".format(round(growth * 100,2)))
    return distribution

import numpy as np
import matplotlib.pyplot as plt
def pop_hist(distribution):
    if len(distribution) == 0:
        print("No histogram.")
        return
    pop = []
    for char in distribution:
        pop += [char]*distribution[char]
    unique = []
    for animal in pop:
        if animal not in unique:
            unique.append(animal)
    ticks_range = list(range(min(unique),max(unique)+2))
    bin_range = [n - 0.5 for n in ticks_range]
    aray, bins, patches = plt.hist(pop, bins=bin_range, weights = np.ones(len(pop)), density = True,\
             edgecolor="black", linewidth=0.8)
    prime_pos = []
    for animal in unique:
        if is_prime(animal) and animal > 5:
            prime_pos.append(animal - min(unique))
    for prime in prime_pos:
        patches[prime].set_fc("green")
    plt.xticks(ticks_range)
    plt.grid(visible = True, which = "major", axis = "y")
    plt.show()




if __name__ == '__main__':
    print("Statistical analysis of the evolution of a population.")
    pop_string = input("Please enter the characteristics of the starting population, separating numbers with commas: ")
    pop = [int(s) for s in pop_string.split(',')]
    n_string = input("To which generation should the population evolve? ")
    runs_string = input("How many times should the simulation be run? ")
    print("-----")
    print("Simulating")
    print("-----")
    distribution = statistical_n(pop,int(n_string),int(runs_string))
    pop_hist(distribution)
    
