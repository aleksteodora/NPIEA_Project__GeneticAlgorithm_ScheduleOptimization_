import random
import copy
from individual import Individual, DAYS, START_TIME, END_TIME, TIME_STEP
from utils import is_valid_placement


def generate_valid_start_time(duration):
    valid_start_times = list(range(START_TIME, END_TIME - duration + 1, TIME_STEP))
    return random.choice(valid_start_times)


def crossover_by_event_safe(parent1, parent2, rooms):
    # mapiranje dogadjaja po imenu za oba roditelja
    p1_map = {ev["name"]: ev for ev in parent1.timetable}
    p2_map = {ev["name"]: ev for ev in parent2.timetable}

    child_events = []

    for name in p1_map:
        # izbor nasumicno jednog roditelja za dogadjaj
        chosen = random.choice([p1_map[name], p2_map[name]])
        candidate = copy.deepcopy(chosen)

        # provera da li kandidat moze da se doda bez konflikta
        if is_valid_placement(candidate, child_events):
            child_events.append(candidate)
            continue

        # alternativa iz drugog roditelja
        alt = p1_map[name] if chosen == p2_map[name] else p2_map[name]
        alt_candidate = copy.deepcopy(alt)
        if is_valid_placement(alt_candidate, child_events):
            child_events.append(alt_candidate)
            continue

        # ako ni jedan od roditelja ne moze, generisi novu validnu poziciju
        duration = candidate["duration"]
        for _ in range(1000):  # sigurnosna granica pokusaja
            candidate["day"] = random.choice(DAYS)
            candidate["start_time"] = generate_valid_start_time(duration)
            candidate["room"] = random.choice(rooms)

            if is_valid_placement(candidate, child_events):
                child_events.append(copy.deepcopy(candidate))
                break

    # kreiraj potomka kao Individual sa definisanim rasporedom
    child = Individual([], rooms)
    child.timetable = child_events
    return child
