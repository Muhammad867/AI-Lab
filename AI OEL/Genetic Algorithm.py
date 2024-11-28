import random

# Step 2: Define the fitness function
def fitness_function(x):
    return x ** 2

# Step 3: Randomly generate an initial population
def initialize_population(pop_size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(pop_size)]

# Step 5: Select parents based on fitness (roulette wheel selection)
def select_parents(population, fitnesses):
    total_fitness = sum(fitnesses)
    probabilities = [f / total_fitness for f in fitnesses]
    return random.choices(population, weights=probabilities, k=2)

# Step 6: Crossover operation
def crossover(parent1, parent2, crossover_probability):
    if random.random() < crossover_probability:
        crossover_point = random.randint(1, len(bin(parent1)) - 3)
        mask = (1 << crossover_point) - 1
        child1 = (parent1 & mask) | (parent2 & ~mask)
        child2 = (parent2 & mask) | (parent1 & ~mask)
        return child1, child2
    return parent1, parent2

# Step 6: Mutation operation
def mutate(individual, mutation_probability, lower_bound, upper_bound):
    if random.random() < mutation_probability:
        bit_to_flip = random.randint(0, len(bin(individual)) - 3)
        individual ^= (1 << bit_to_flip)
        individual = max(lower_bound, min(upper_bound, individual))
    return individual

# Main Genetic Algorithm function
def genetic_algorithm(pop_size, generations, lower_bound, upper_bound, crossover_probability, mutation_probability):
    # Step 3: Initialize the population
    population = initialize_population(pop_size, lower_bound, upper_bound)

    for generation in range(generations):
        # Step 4: Evaluate fitness
        fitnesses = [fitness_function(ind) for ind in population]

        # Step 5-8: Create a new population
        new_population = []
        while len(new_population) < pop_size:
            parent1, parent2 = select_parents(population, fitnesses)
            child1, child2 = crossover(parent1, parent2, crossover_probability)
            child1 = mutate(child1, mutation_probability, lower_bound, upper_bound)
            child2 = mutate(child2, mutation_probability, lower_bound, upper_bound)
            new_population.extend([child1, child2])

        # Step 9: Replace the old population with the new one
        population = new_population[:pop_size]

        # Log the best solution so far
        best_individual = max(population, key=fitness_function)
        print(f"Generation {generation + 1}: Best = {best_individual}, Fitness = {fitness_function(best_individual)}")

        # Step 10: Termination criterion (e.g., max fitness or max generations)
        if max(fitnesses) == fitness_function(upper_bound):  # Ideal fitness reached
            break

    return max(population, key=fitness_function)

# Parameters
POP_SIZE = 50
GENERATIONS = 100
LOWER_BOUND = 0
UPPER_BOUND = 31
CROSSOVER_PROBABILITY = 0.7
MUTATION_PROBABILITY = 0.2

# Run the Genetic Algorithm
best_solution = genetic_algorithm(
    POP_SIZE, GENERATIONS, LOWER_BOUND, UPPER_BOUND, CROSSOVER_PROBABILITY, MUTATION_PROBABILITY
)
print(f"\nBest Solution: {best_solution}, Fitness: {best_solution ** 2}")
