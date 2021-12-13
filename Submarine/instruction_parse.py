import functools as fn

#Write the instructions
class InstructionBlock:
    def __init__(self, movement, amount):
        self.movement = movement
        self.amount = (int)(amount)
        self.summer = 0
    def __str__(self) -> str:
        return self.movement
    def horizontal(self):
        return (self.amount if self.movement == "forward" else 0)
    def vertical(self):
        if self.movement == "down" :
            return self.amount
        elif self.movement == "up" :
            return -self.amount
        else :
            return 0


#Build the sub
class CurrentPosition:
    def __init__(self):
        self.aim = 0
        self.horizontal = 0
        self.depth = 0
    def instruction(self, instruct):
        self.aim += instruct.vertical()
        self.horizontal += instruct.horizontal()
        self.depth += self.aim * instruct.horizontal()
        return self
    def __str__(self) -> str:
        return "Aim : %i - Forward : %i - Depth : %i - Total : %i" % (self.aim, self.horizontal, self.depth, (self.horizontal*self.depth))

#Day 2 Part 1
def move_with_instructions(list_of_strings):
    move_list = list(map(lambda x : InstructionBlock(x.split(" ")[0],x.split(" ")[1]), list_of_strings))

    horizontal = 0
    vertical = 0

    horizontal = fn.reduce(lambda x, y : x + y.horizontal(), move_list, horizontal)
    vertical = fn.reduce(lambda x, y : x + y.vertical(), move_list, vertical)

    total = horizontal * vertical

    print("Horizontal distance %i * Vertical Distance %i = Total %i " % (horizontal, vertical, total))

#Day 2 Part 2
def move_with_aim_and_depth(list_of_strings):
    #could probably unit test this...
    #list_of_strings = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

    #convert strings into more useful formats.
    list_of_instructions = list(map(lambda x : InstructionBlock(x.split(" ")[0],x.split(" ")[1]), list_of_strings))

    return fn.reduce(lambda sub, instr : sub.instruction(instr), list_of_instructions, CurrentPosition())