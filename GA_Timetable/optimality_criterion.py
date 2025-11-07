START_TIME = 420  # 07:00 u minutima
END_TIME = 1140   # 19:00 u minutima

def calculate_optimality_criterion(individual):
    timetable = individual.timetable
    rooms = individual.rooms

    # inicijalizujemo mapu: (dan, učionica) -> lista dogadjaja
    day_room_events = {
        (day, room): [] for day in range(5) for room in rooms
    }

    # grupisanje dogadjaja po danu i ucionici
    for event in timetable:
        key = (event['day'], event['room'])
        day_room_events[key].append(event)

    total_score = 0

    for (day, room), events in day_room_events.items():
        if not events:
            # ako tog dana u toj ucionici nema nastave -> pi = 720, ki = 0 -> pi * ki = 0
            continue

        # nadji najraniji pocetak i najkasniji kraj
        start_times = [e['start_time'] for e in events]
        end_times = [e['start_time'] + e['duration'] for e in events]

        earliest = min(start_times)
        latest = max(end_times)

        pi = earliest - START_TIME
        ki = END_TIME - latest

        # ako je nesto slucajno van dozvoljenog vremenskog opsega, postavi na 0
        pi = max(0, pi)
        ki = max(0, ki)

        total_score += pi * ki

    return total_score
