def did_everyone_answer_question(question, responses):
    return all([question in response for response in responses])

def count_questions_everyone_answered(questions_answered, responses):
    questions_everyone_answered = []
    for q in questions_answered:
        if did_everyone_answer_question(q, responses):
            questions_everyone_answered.append(q)
    return len(questions_everyone_answered)

input_file = open("input.txt", "r")
all_responses = input_file.read().split("\n\n")
input_file.close()

responses_by_group = [a.split("\n") for a in all_responses]

# Part 1
questions_answered_per_group = [
    set([question for answers in group for question in answers]) 
    for group in responses_by_group
]
    
print("(Day 6: Part 1) Result: " + str(sum([len(q) for q in questions_answered_per_group])))

# Part 2

num_questions_everyone_answered_per_group = [
    count_questions_everyone_answered(
        questions_answered_per_group[index],
        group
    ) 
    for index, group in enumerate(responses_by_group)
]

print("(Day 6: Part 2) Result: " + str(sum(num_questions_everyone_answered_per_group)))
