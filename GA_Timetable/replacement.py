def replace_population(old_individuals, old_scores, offspring, offspring_scores, population_size, elite_size=2):
    # sortiraj po kriterijumu opadajuce (najbolji prvi)
    elite = sorted(zip(old_individuals, old_scores), key=lambda x: x[1], reverse=True)[:elite_size]

    rest_needed = population_size - elite_size

    # najbolji potomci
    rest = sorted(zip(offspring, offspring_scores), key=lambda x: x[1], reverse=True)[:rest_needed]

    # ako nema dovoljno potomaka, popuni iz stare populacije osim elite
    if len(rest) < rest_needed:
        # stara populacija bez elite
        old_remaining = sorted(zip(old_individuals, old_scores), key=lambda x: x[1], reverse=True)[elite_size:]
        needed = rest_needed - len(rest)
        rest += old_remaining[:needed]

    # sastavi novu populaciju
    new_individuals = [ind for ind, _ in elite + rest]

    # uveri se da je velicina tacna
    assert len(new_individuals) == population_size, "Pogrešna veličina nove populacije"

    return new_individuals
