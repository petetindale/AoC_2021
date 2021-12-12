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
        


def movement_str(move):
    return Vector(move.split(" ")[0],move.split(" ")[1])

def horizontalCount(move1, move2):
    move1.amount = move1.amount + move2.amount
    return move1

        
test = movement_str("up 9")

print(test.horizontal())
print(test.vertical())

f = open("/Users/petertindale/Source/AoC-python/Day2/list.txt", "r")

move_list = f.readlines()

f.close()

#print(move_list)


move_list = list(map(movement_str, move_list))

hor = fn.reduce(horizontalCount, move_list)

print(hor.amount)


#print(move_list[0].movement)
#print(move_list[1].amount)