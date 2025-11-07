import random
from copy import deepcopy
from utils import is_valid_schedule
from individual import Individual, DAYS, START_TIME, END_TIME, TIME_STEP

def mutate(individual, mutation_rate=0.1):
    new_ind = individual.clone()

    for i, event in enumerate(new_ind.timetable):
        if random.random() < mutation_rate:
            for _ in range(10):
                mutated_event = deepcopy(event)
                attr_to_change = random.choice(["day", "start_time", "room"])

                if attr_to_change == "day":
                    mutated_event["day"] = random.choice(DAYS)

                elif attr_to_change == "start_time":
                    latest_start = END_TIME - mutated_event["duration"]
                    mutated_event["start_time"] = random.randrange(
                        START_TIME, latest_start + 1, TIME_STEP
                    )

                elif attr_to_change == "room":
                    mutated_event["room"] = random.choice(new_ind.rooms)

                # proveri validnost
                temp_schedule = new_ind.timetable[:i] + [mutated_event] + new_ind.timetable[i+1:]
                if is_valid_schedule(temp_schedule):
                    new_ind.timetable[i] = mutated_event
                    break

    return new_ind
