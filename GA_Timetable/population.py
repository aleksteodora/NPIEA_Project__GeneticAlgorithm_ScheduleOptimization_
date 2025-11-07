from individual import Individual
from optimality_criterion import calculate_optimality_criterion

class Population:

    def __init__(self, size, events, rooms, max_attempts_per_individual=20):
        self.individuals = []
        self.scores = []

        for _ in range(size):
            for _ in range(max_attempts_per_individual):
                candidate = Individual(events, rooms)
                if candidate.timetable is not None:
                    self.individuals.append(candidate)
                    break  # predji na sledecu jedinku
            # ako posle max_attempts_per_individual ne uspe, ignorise se ta jedinka


    def evaluate(self):
        self.scores = []
        for individual in self.individuals:
            value = calculate_optimality_criterion(individual)
            individual.criterion_value = value
            self.scores.append(value)


    def get_best(self):
        if not self.scores:
            self.evaluate()

        max_index = self.scores.index(max(self.scores))
        return self.individuals[max_index], self.scores[max_index]
