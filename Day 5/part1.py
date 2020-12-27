import re

input_file = open("input.txt", "r")
boarding_passes = input_file.read().split("\n")
input_file.close()

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

seat_ids = []
for b in boarding_passes:
    row_string, col_string = re.compile(r"([BF]+)([LR]+)").search(b).groups()
    row = seat_binary_search({"min": 0, "max": 127}, row_string)
    column = seat_binary_search({"min": 0, "max": 7}, col_string)
    seat_ids.append((row * 8 + column))
    boarding_pass_info.append({
        "boarding_pass": b,
        "row": row, 
        "col": column,
        "seat_id": row * 8 + column
    })
