import random

# Distance matrix representing distances between cities
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
]

# Number of cities
num_cities = len(distance_matrix)

# Fitness function: inverse of the total distance of the route
def fitness_function(route):
    total_distance = sum(
        distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1)
    )
    total_distance += distance_matrix[route[-1]][route[0]]
    return 1 / total_distance

# Generate initial population of random routes
def generate_population(pop_size, num_cities):
    return [random.sample(range(num_cities), num_cities) for _ in range(pop_size)]


def select_parents(population, fitnesses):
    total_fitness = sum(fitnesses)
    probabilities = [f / total_fitness for f in fitnesses]
    return random.choices(population, weights=probabilities, k=2)


def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(num_cities), 2))
    child = [-1] * num_cities
    child[start:end + 1] = parent1[start:end + 1]

    pointer = 0
    for gene in parent2:
        if gene not in child:
            while child[pointer] != -1:
                pointer += 1
            child[pointer] = gene

    return child


def mutate(route, mutation_rate):
    if random.random() < mutation_rate:
        i, j = random.sample(range(num_cities), 2)
        route[i], route[j] = route[j], route[i]
    return route

# Main Genetic Algorithm function
def genetic_algorithm(
    distance_matrix,
    pop_size,
    generations,
    crossover_probability,
    mutation_probability,
):
    # Step 1: Generate initial population
    population = generate_population(pop_size, num_cities)

    for generation in range(generations):
        # Step 2: Calculate fitness of each individual
        fitnesses = [fitness_function(route) for route in population]

        # Step 3: Create new population
        new_population = []
        while len(new_population) < pop_size:
            # Step 4: Selection
            parent1, parent2 = select_parents(population, fitnesses)

            # Step 5: Crossover
            if random.random() < crossover_probability:
                child = crossover(parent1, parent2)
            else:
                child = parent1[:]

            # Step 6: Mutation
            child = mutate(child, mutation_probability)

            new_population.append(child)

        # Step 7: Replace old population with new population
        population = new_population

        # Log the best route of the generation
        best_route = max(population, key=fitness_function)
        best_distance = 1 / fitness_function(best_route)
        print(
            f"Generation {generation + 1}: Best Route = {best_route}, Distance = {best_distance}"
        )

    # Return the best solution
    best_route = max(population, key=fitness_function)
    best_distance = 1 / fitness_function(best_route)
    return best_route, best_distance


# Parameters
POP_SIZE = 10
GENERATIONS = 50
CROSSOVER_PROBABILITY = 0.8
MUTATION_PROBABILITY = 0.2

# Solve TSP using Genetic Algorithm
best_route, best_distance = genetic_algorithm(
    distance_matrix,
    POP_SIZE,
    GENERATIONS,
    CROSSOVER_PROBABILITY,
    MUTATION_PROBABILITY,
)
print(f"\nBest Route: {best_route}, Distance: {best_distance}")
