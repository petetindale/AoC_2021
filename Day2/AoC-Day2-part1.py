import sys
import functools as fn

print(sys.version)

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
        

f = open("/Users/petertindale/Source/AoC-python/Day2/list.txt", "r")

move_list = f.readlines()

f.close()

#print(move_list)


move_list = list(map(lambda x : Vector(x.split(" ")[0],x.split(" ")[1]), move_list))

horizontal = 0
vertical = 0

horizontal = fn.reduce(lambda x, y : x + y.horizontal(), move_list, horizontal)
vertical = fn.reduce(lambda x, y : x + y.vertical(), move_list, vertical)

total = horizontal * vertical

print("Horizontal distance %i * Vertical Distance %i = Total %i " % (horizontal, vertical, total))

