import random

def calculate_ranks(individuals):
    sorted_individuals = sorted(individuals, key=lambda ind: ind.criterion_value)
    ranked = [(i + 1, ind) for i, ind in enumerate(sorted_individuals)]
    return ranked


def select_parents(population, num_parents):
    ranked = calculate_ranks(population.individuals)

    scores = []
    for rank, ind in ranked:
        r = random.random()
        score = rank * r
        scores.append((score, ind))

    # biramo num_parents jedinki sa NAJVEcIM score-ovima (sto je bolje)
    selected = sorted(scores, key=lambda pair: pair[0], reverse=True)[:num_parents]
    return [ind for _, ind in selected]
