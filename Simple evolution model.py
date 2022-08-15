from random import randint
import numpy as np
import matplotlib.pyplot as plt


def mutate(offspring):
    new = []
    for baby in offspring:
        roll = randint(1, 6)
        if roll == 1:
            new.append(baby - 1)
        elif roll == 6:
            new.append(baby + 1)
        else:
            new.append(baby)
    return new


def reproduce(parents, printing):
    offspring = mutate(parents) + mutate(parents)
    if printing:
        print(f"The offspring are {offspring}")
    return offspring


def select(pop, printing):
    predator = randint(2, 6)
    if printing:
        print(f"The predator number is {predator}")
    survivors = []
    for animal in pop:
        if animal % predator != 0:
            survivors.append(animal)
    if printing:
        if len(survivors) == 0:
            print("The population has gone extinct.")
        else:
            print(f"The survivors are {survivors}")
    return survivors


def evolve(pop, printing):
    return select(reproduce(pop, printing), printing)


def ordinal(n):
    if n == 1:
        return "st"
    elif n == 2:
        return "nd"
    elif n == 3:
        return "rd"
    else:
        return "th"


def gen_n(pop, n, printing):
    # Generates the nth generation, where pop is the 1st generation
    if printing:
        print(f"The starting generation is {pop}")
    if n == 1:
        if printing:
            print("This is the 1st generation.")
        return pop
    result = pop
    for i in range(1, n):
        result = evolve(result, printing)
    if printing:
        max_pop_size = len(pop) * 2 ** (n - 1)
        print(f"This is the {n}{ordinal(n)} generation, of size {len(result)} of a maximum of {max_pop_size}, "
              f"which is {(len(result) / max_pop_size) * 100}%.")
    return result


def is_prime(n):
    if n < 3:
        return False
    for i in range(2, int(n / 2)):
        if (n % i) == 0:
            return False
    return True


def vulnerability(n):
    result = 0
    for i in range(2, 7):
        if n % i == 0:
            result += 1
    return result


def pop_stats(pop):
    print(f"The population size is {len(pop)}")
    unique = []
    for animal in pop:
        if animal not in unique:
            unique.append(animal)
    unique.sort()
    print("...")
    print(f"The extant characteristics are {unique}")
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
    print(f"The proportion of animals with a prime number characteristic is {round(primes_prop, 2)}%.")
    vuln_index = 0
    for char in unique:
        vuln_index += vulnerability(char) * proportion[char] / 100
    print("...")
    print(f"The vulnerability index is {round(vuln_index, 2)}, compared to a maximum of 5.")
    return distribution


def ave_growth(initial, final, n):
    return (final / initial) ** (1 / (n - 1)) - 1


def analyse_n(pop, n):
    print("Analysis of the {0}{1} generation given the founding population {2}:".format(n, ordinal(n), pop))
    result = pop_stats(gen_n(pop, n, False))
    pop_size = 0
    for char in result:
        pop_size += result[char]
    growth = ave_growth(len(pop), pop_size, n)
    print(f"The average growth rate is {round(growth * 100, 2)}% per generation, compared to a maximum of 100%.")


def statistical_n(pop, n, runs):
    print(f"Statistical analysis of the {n}{ordinal(n)} generation given the founding population {pop} "
          f"from {runs} simulations:")
    result = []
    for i in range(runs):
        result += gen_n(pop, n, False)
    distribution = pop_stats(result)
    growth = ave_growth(len(pop) * runs, len(result), n)
    print("...")
    print(f"The average growth rate is {round(growth * 100, 2)}% per generation, compared to a maximum of 100%.")
    return distribution


def pop_hist(distribution):
    if len(distribution) == 0:
        print("No histogram.")
        return
    pop = []
    for char in distribution:
        pop += [char] * distribution[char]
    unique = []
    for animal in pop:
        if animal not in unique:
            unique.append(animal)
    ticks_range = list(range(min(unique), max(unique) + 2))
    bin_range = [n - 0.5 for n in ticks_range]
    aray, bins, patches = plt.hist(pop, bins=bin_range, weights=np.ones(len(pop)), density=True,
                                   edgecolor="black", linewidth=0.8)
    prime_pos = []
    for animal in unique:
        if is_prime(animal) and animal > 5:
            prime_pos.append(animal - min(unique))
    for prime in prime_pos:
        patches[prime].set_fc("green")
    plt.xticks(ticks_range)
    plt.grid(visible=True, which="major", axis="y")
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
    distribution = statistical_n(pop, int(n_string), int(runs_string))
    pop_hist(distribution)
