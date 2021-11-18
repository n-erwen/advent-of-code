class Day2:
    @staticmethod
    def read_input(filename):
        with open(filename, "r") as f:
            return f.read()
        
    @staticmethod
    def run_intcode_program(program):
        instrucs = [int(i) for i in program.split(",")]
        n = 0
        while instrucs[n] != 99:
            if instrucs[n] == 1:
                instrucs[instrucs[n+3]] = instrucs[instrucs[n+1]] + instrucs[instrucs[n+2]]
            elif instrucs[n] == 2:
                instrucs[instrucs[n+3]] = instrucs[instrucs[n+1]] * instrucs[instrucs[n+2]]
            n += 4
        return ",".join([str(i) for i in instrucs])
    
    @staticmethod
    def modify_program_with_inputs(program, pos1, pos2):
        instrucs = [int(i) for i in program.split(",")]
        instrucs[1] = pos1
        instrucs[2] = pos2
        return ",".join([str(i) for i in instrucs])
    
    
    @classmethod
    def get_program_output(cls, program):
        return cls.run_intcode_program(program).split(",")[0]

class Day2Part2(Day2):
    @classmethod
    def getTargetPair(cls, prog, target):
        for noun in range(100):
            for verb in range(100):
                prog = cls.modify_program_with_inputs(prog, noun, verb)
                output = cls.get_program_output(prog)
                if int(output) == target:
                    return [noun, verb]
        return [-1, -1]

if __name__ == "__main__":
    prog = Day2.read_input("input.txt") 
    part_1_result = Day2.get_program_output(Day2.modify_program_with_inputs(
        prog,
        pos1=12,
        pos2=2
    ))
    print("\nPart 1 Result: {}".format(part_1_result))
    
    prog = Day2.read_input("input.txt")
    noun, verb = Day2Part2.getTargetPair(prog, 19690720)
    assert noun > 0 and verb > 0, "wrong pair!"
    print("Part 2 Result: {}".format(100 * noun + verb))
