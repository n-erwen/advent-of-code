import re

def seat_binary_search(bounds, search_pattern, index=0):
    if bounds["min"] != bounds["max"]:
        if search_pattern[index] == "F" or search_pattern[index] == "L" :
            return seat_binary_search({
                "min": bounds["min"],
                "max": (bounds["min"] + bounds["max"]) // 2
            }, search_pattern, index=index+1)
        elif search_pattern[index] == "B" or search_pattern[index] == "R":
            return seat_binary_search({
                "min": (bounds["min"] + bounds["max"]) // 2 + 1,
                "max": bounds["max"]
            }, search_pattern, index=index+1)
    return bounds["min"]

def find_my_seat_id(seat_ids):
    missing_seat_ids = [s for s in range(1024) if s not in seat_ids]
    for s in missing_seat_ids:
        if (s-1 in seat_ids) and (s+1 in seat_ids):
            return s
    return None

if __name__ == "__main__":
    input_file = open("input.txt", "r")
    boarding_passes = input_file.read().split("\n")
    input_file.close()

    seat_ids = []
    for b in boarding_passes:
        row_string, col_string = re.compile(r"([BF]+)([LR]+)").search(b).groups()
        row = seat_binary_search({"min": 0, "max": 127}, row_string)
        column = seat_binary_search({"min": 0, "max": 7}, col_string)
        seat_ids.append((row * 8 + column))

    print("(Day 5: Part 1) Highest Seat ID: " + str(max(seat_ids)))
    print("(Day 5: Part 2) My Seat ID: " + str(find_my_seat_id(seat_ids)))
