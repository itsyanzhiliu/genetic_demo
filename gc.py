import random
import string
import time

TARGET_STRING = "Everything Apple announced today: Apple Watch 8 and SE, Apple One, new iPad Air. The Apple Store went down this morning, heralding another Apple launch day. At the company's virtual event, Tim Cook started out by telling us that the Apple Watch and new additions to the iPad family of tablets would be the highlights -- and we got an Apple Watch Series 8, Apple Watch SE, a redesigned iPad Air debuting the A14 Bionic chip and a new eighth-gen iPad."
POPULATION_SIZE = 100
MUTATION_RATE = 0.1
GENERATIONS = 1000
STATS_INTERVAL = 50


def generate_random_chromosome(target_length):
    return ''.join(random.choice(string.printable) for _ in range(target_length))


def evaluate_fitness(chromosome):
    return sum(1 for i, j in zip(chromosome, TARGET_STRING) if i != j)


def select_parents(population, num_parents):
    parents = []
    for _ in range(num_parents):
        parent = random.choice(population)
        parents.append(parent)
    return parents


def crossover(parent1, parent2):
    midpoint = random.randint(0, len(parent1))
    child = parent1[:midpoint] + parent2[midpoint:]
    return child


def mutate(chromosome):
    mutated = list(chromosome)
    for i in range(len(mutated)):
        if random.random() < MUTATION_RATE:
            mutated[i] = random.choice(string.printable)
    return ''.join(mutated)


def main():
    start_time = time.time()
    population = [generate_random_chromosome(len(TARGET_STRING)) for _ in range(POPULATION_SIZE)]

    for generation in range(GENERATIONS + 1):
        population.sort(key=lambda chrom: evaluate_fitness(chrom))
        best_fit = population[0]

        if evaluate_fitness(best_fit) == 0:
            print(
                f"done: {GENERATIONS * POPULATION_SIZE} evaluated chromosomes, {generation} generations, best fit 0 (perfect sol)")
            print(f"{TARGET_STRING}")
            break

        if generation % STATS_INTERVAL == 0:
            avg_fitness = sum(evaluate_fitness(chrom) for chrom in population) / len(population)
            print(f"generation {generation}, average fit {avg_fitness:.2f}, best fit {evaluate_fitness(best_fit)}")
            print(f"'{best_fit}'")

        new_population = [best_fit]  # Keep the best individual

        while len(new_population) < POPULATION_SIZE:
            parents = select_parents(population, 2)
            child = crossover(parents[0], parents[1])
            child = mutate(child)
            new_population.append(child)

        population = new_population

    print(
        f"done: {GENERATIONS * POPULATION_SIZE} evaluated chromosomes, {GENERATIONS} generations, best fit {evaluate_fitness(best_fit)}")
    print(f"{TARGET_STRING}")
    print(f"Total runtime: {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    main()