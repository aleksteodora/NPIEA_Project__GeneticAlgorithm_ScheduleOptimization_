from collections import defaultdict

def is_valid_schedule(schedule):
    # provera uslova
    # dan od 0 do 4
    # start_time >= 420
    # end_time <= 1140
    # izmedju termina u istoj ucionici i danu postoji >= 15 min pauze

    START = 420
    END = 1140

    events_by_room_day = defaultdict(list)

    for event in schedule:
        day = event["day"]
        start = event["start_time"]
        end = start + event["duration"]

        if not (0 <= day <= 4):
            return False
        if start < START or end > END:
            return False

        # grupisanje po ucionici i danu
        key = (event["room"], event["day"])
        events_by_room_day[key].append(event)

    for group in events_by_room_day.values():
        sorted_events = sorted(group, key=lambda e: e["start_time"])
        for i in range(1, len(sorted_events)):
            prev = sorted_events[i - 1]
            curr = sorted_events[i]

            prev_end = prev["start_time"] + prev["duration"]
            if curr["start_time"] < prev_end + 15:
                return False

    return True


def is_valid_placement(event, current_schedule):
    for e in current_schedule:
        if e["day"] != event["day"]:
            continue
        if e["room"] != event["room"]:
            continue

        start1 = e["start_time"]
        end1 = start1 + e["duration"]
        start2 = event["start_time"]
        end2 = start2 + event["duration"]

        # mora postojati bar 15 min pauze
        if not (end1 + 15 <= start2 or end2 + 15 <= start1):
            return False

    return True


def format_schedule_by_day(timetable):
    # formatira raspored po danima i vremenima za ispis u fajl

    day_names = ["Ponedeljak", "Utorak", "Sreda", "Cetvrtak", "Petak"]
    timetable_sorted = sorted(timetable, key=lambda e: (e["day"], e["start_time"]))
    
    result = []
    for day in range(5):
        day_events = [e for e in timetable_sorted if e["day"] == day]
        if not day_events:
            continue
        result.append(f"\n📅 {day_names[day]}")
        for event in day_events:
            start = event["start_time"]
            end = start + event["duration"]
            h1, m1 = start // 60, start % 60
            h2, m2 = end // 60, end % 60
            line = f"🕓 {h1:02d}:{m1:02d} - {h2:02d}:{m2:02d} | {event['name']} (ucionica: {event['room']})"
            result.append(line)
    return "\n".join(result)


def save_room_occupancy(timetable, file_path):
    # upisuje zauzece ucionica u fajl

    from collections import defaultdict

    rooms = defaultdict(list)
    for event in timetable:
        rooms[event["room"]].append(event)

    with open(file_path, "w", encoding="utf-8") as f:
        for room, events in sorted(rooms.items()):
            f.write(f"\n🏫 Ucionica: {room}\n")
            for event in sorted(events, key=lambda e: (e["day"], e["start_time"])):
                start = event["start_time"]
                end = start + event["duration"]
                h1, m1 = start // 60, start % 60
                h2, m2 = end // 60, end % 60
                day_name = ["Ponedeljak", "Utorak", "Sreda", "Cetvrtak", "Petak"][event["day"]]
                f.write(f"🕓 {h1:02d}:{m1:02d} - {h2:02d}:{m2:02d} | {event['name']} ({day_name})\n")
