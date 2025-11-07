def load_rooms(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        line = f.readline().strip()
        rooms = line.split(":")[1].strip().split(", ")
    return rooms


def load_events(file_path):
    events = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()[2:]  # preskace 1. i 2. liniju
        for line in lines:
            if line.strip() == "":
                continue
            name, duration = line.strip().rsplit(",", 1)
            events.append((name.strip(), int(duration.strip())))
    return events
