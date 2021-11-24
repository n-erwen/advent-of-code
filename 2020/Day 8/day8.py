def load_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().split('\n')

# Part 1

def run_instruction(instr, index, accum):
    operand, arg = instr.split(" ")    
    if operand == "jmp":
        index += int(arg)
    else:
        if operand == "acc":
            accum += int(arg)
        index += 1
    return accum, index

def run_each_instruction_only_once(prog):
    accum, index, history = 0, 0, [] 
    while index < len(prog):
        if index in history:
            return accum, "failure"
        history.append(index)
        accum, index = run_instruction(prog[index], index, accum)
    return accum, "success"

    
# part 2

def replace_operand(prog, index):
    if "jmp" in prog[index]:
        old, new = "jmp", "nop"
    elif "nop" in prog[index]:
        old, new = "nop", "jmp"
    prog[index] = prog[index].replace(old, new)
    return prog

def fix_program(prog):
    jmp_nop_instructions = [index for index, instr in enumerate(prog) if ("jmp" in instr or "nop" in instr)]
    for i in jmp_nop_instructions:
        new_prog = replace_operand(prog.copy(), i)
        status = run_each_instruction_only_once(new_prog)[1]
        if status == "success":
            return new_prog

def get_accum_value_of_fixed_program(prog):
    return run_each_instruction_only_once(fix_program(prog))[0]

###

if __name__ == "__main__":
    program = load_input('./input.txt')
    print("(Day 8 Part 1) Value of accumulator before an instruction is run twice: {} ".format(
        run_each_instruction_only_once(program)[0]
    ))
    print("(Day 8 Part 2) Value of accumulator when fixed program terminates: {} ".format(
        get_accum_value_of_fixed_program(program)
    ))
