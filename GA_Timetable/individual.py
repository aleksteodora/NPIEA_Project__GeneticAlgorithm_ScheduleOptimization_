import random
import copy
from collections import defaultdict

DAYS = [0, 1, 2, 3, 4]          # 0 = pon, 1 = uto itd
START_TIME = 420                # 07:00 u minutima
END_TIME = 1140                 # 19:00 u minutima
TIME_STEP = 15                  # pocetak mora biti deljiv sa 15

class Individual:

    def __init__(self, events, rooms):
        self.rooms = rooms
        self.timetable = []
        self.criterion_value = None

        occupied = defaultdict(list)

        for name, duration in events:
            placed = False
            latest_start = END_TIME - duration

            for day in random.sample(DAYS, len(DAYS)):
                for room in random.sample(rooms, len(rooms)):
                    for start_time in range(latest_start, START_TIME - 1, -TIME_STEP):
                        end_time = start_time + duration
                        if end_time > END_TIME:
                            continue

                        busy = occupied[(room, day)]
                        if all(end_time + 15 <= b[0] or start_time >= b[1] + 15 for b in busy):
                            occupied[(room, day)].append((start_time, end_time))
                            self.timetable.append({
                                "name": name,
                                "duration": duration,
                                "day": day,
                                "room": room,
                                "start_time": start_time
                            })
                            placed = True
                            break
                    if placed:
                        break
                if placed:
                    break

            if not placed:
                # ako bar jedan događaj ne moze da se smesti, ponisti celu jedinku
                self.timetable = None
                return


    def __str__(self):
        lines = []
        for event in sorted(self.timetable, key=lambda e: (e["day"], e["start_time"])):
            h = event["start_time"] // 60
            m = event["start_time"] % 60
            lines.append(
                f"{event['name']} | Dan: {event['day']} | Učionica: {event['room']} | Početak: {h:02d}:{m:02d} | Trajanje: {event['duration']} min"
            )
        return "\n".join(lines)
    

    def clone(self):
        return copy.deepcopy(self)
