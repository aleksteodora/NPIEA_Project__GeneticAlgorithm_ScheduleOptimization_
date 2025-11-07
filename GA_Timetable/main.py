from load_data import load_events, load_rooms
from population import Population
from selection import select_parents
from crossover import crossover_by_event_safe
from mutation import mutate
from optimality_criterion import calculate_optimality_criterion
from replacement import replace_population
from utils import format_schedule_by_day, save_room_occupancy, is_valid_schedule

import matplotlib.pyplot as plt

# parametri
POPULATION_SIZE = 100
GENERATIONS = 700
MUTATION_RATE = 0.05
ELITE_SIZE = 5
NUM_PARENTS = 20

def main():
    # ucitavanje podataka
    events = load_events("data/data_timetable.txt")
    rooms = load_rooms("data/data_timetable.txt")

    print("Pocetak evolucije genetskog algoritma...\n")

    # inicijalna populacija
    population = Population(size=POPULATION_SIZE, events=events, rooms=rooms)
    population.evaluate()

    best_history = []

    for gen in range(GENERATIONS):
        parents = select_parents(population, NUM_PARENTS)

        offspring = []
        for i in range(0, len(parents), 2):
            if i + 1 >= len(parents):
                break
            p1 = parents[i]
            p2 = parents[i + 1]

            child = crossover_by_event_safe(p1, p2, rooms)
            mutated_child = mutate(child, mutation_rate=MUTATION_RATE)

            # azuriraj vrednost kriterijuma
            mutated_child.criterion_value = calculate_optimality_criterion(mutated_child)
            offspring.append(mutated_child)

        offspring_scores = [ind.criterion_value for ind in offspring]

        # zamena populacije
        population.individuals = replace_population(
            old_individuals=population.individuals,
            old_scores=population.scores,
            offspring=offspring,
            offspring_scores=offspring_scores,
            population_size=POPULATION_SIZE,
            elite_size=ELITE_SIZE
        )

        population.evaluate()
        best_individual, best_score = population.get_best()
        best_history.append(best_score)

        print(f"Generacija {gen+1}: Najbolji score: {best_score}")

    print("\nEvolucija zavrsena.\n")

    # upis najboljeg rasporeda po danima
    final_schedule = format_schedule_by_day(best_individual.timetable)

    with open("data/final_schedule.txt", "w", encoding="utf-8") as f:
        f.write("Najbolji raspored:\n")
        f.write(final_schedule)

    # upis zauzeca po ucionicama
    save_room_occupancy(best_individual.timetable, "data/room_occupancy.txt")

    # ispis u konzoli
    print(final_schedule)

    # prikaz grafika napretka
    plt.plot(best_history)
    plt.xlabel("Generacija")
    plt.ylabel("Score f(p, k)")
    plt.title("Napredak kroz generacije")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
