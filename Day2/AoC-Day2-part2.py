from os import path
from functools import reduce

#Write the instructions
class Vector:
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
class Submarine:
    def __init__(self):
        self.aim = 0
        self.horizontal = 0
        self.depth = 0
    def instruction(self, instruct):
        self.aim += instruct.vertical()
        self.horizontal += instruct.horizontal()
        self.depth += self.aim * instruct.horizontal()
    def __str__(self) -> str:
        return "Aim : %i - Forward : %i - Depth : %i - Total : %i" % (self.aim, self.horizontal, self.depth, (self.horizontal*self.depth))


#Load file information
f = open(path.dirname(__file__) + "/list.txt", "r")
move_list = f.readlines()
f.close()

#could probably unit test this...
#move_list = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

#convert strings into more useful formats.
move_list = list(map(lambda x : Vector(x.split(" ")[0],x.split(" ")[1]), move_list))

def move_submarine(sub, instruction):
    return sub.instruction(instruction)

sub = Submarine()

for instruction in move_list:
    sub.instruction(instruction)

print(sub)




