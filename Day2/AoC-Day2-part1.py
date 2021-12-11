import sys
import functools as fn

print(sys.version)

class Vector:
    def __init__(self, movement, amount):
        self.movement = movement
        self.amount = amount
    def __str__(self) -> str:
        return self.movement
    def horizontal(self):
        return (self.amount if self.movement == "forward" else 0)



        


f = open("/Users/petertindale/Source/AoC-python/Day2/list.txt", "r")

move_list = f.readlines()

f.close()

print(move_list)

subVector = tuple[str, int]

move_list = list(map(lambda x : Vector(x.split(" ")[0],x.split(" ")[1]), move_list))

hor = fn.reduce((lambda x, y : x.horizontal()), move_list)

print(move_list[0].movement)
print(move_list[1].amount)