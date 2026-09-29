import os

FILE_NAME = "attendance_data.txt"

def load_data():
    courses = []
    if not os.path.exists(FILE_NAME):
        return courses
    with open(FILE_NAME, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                parts = line.split(",")
                courses.append({
                    "code": parts[0],
                    "name": parts[1],
                    "total": int(parts[2]),
                    "attended": int(parts[3])
                })
    return courses

def save_data(courses):
    with open(FILE_NAME, "w") as f:
        for c in courses:
            f.write(f"{c['code']},{c['name']},{c['total']},{c['attended']}\n")

def get_percentage(attended, total):
    if total == 0:
        return 0.0
    return round((attended / total) * 100, 2)

def calculate_safe_bunks(attended, total, threshold=75.0):
    if total == 0:
        return 0
    bunks = 0
    temp_total = total
    while True:
        if (attended / (temp_total + 1)) * 100 >= threshold:
            bunks += 1
            temp_total += 1
        else:
            break
    return bunks

def calculate_needed_classes(attended, total, threshold=75.0):
    if total == 0 or (attended / total) * 100 >= threshold:
        return 0
    needed = 0
    curr_att = attended
    curr_tot = total
    while (curr_att / curr_tot) * 100 < threshold:
        curr_att += 1
        curr_tot += 1
        needed += 1
    return needed

def find_course(courses, code):
    for c in courses:
        if c["code"].lower() == code.strip().lower():
            return c
    return None