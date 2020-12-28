input_file = open("input.txt", "r")
all_responses = input_file.read().split("\n\n")
input_file.close()

responses_by_group = [a.split("\n") for a in all_responses]

# Part 1
num_of_questions_answered_by_group = []
for group in responses_by_group:
    questions_answered = set([question for answers in group for question in answers])
    num_of_questions_answered_by_group.append(len(questions_answered))
    
print("(Day 6: Part 1) Result: " + str(sum(num_of_questions_answered_by_group)))