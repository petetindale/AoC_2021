from os import path

f = open(path.dirname(__file__) + "/list.txt", "r")
depth_list = f.readlines()

f.close()


z = None
i=0
j=0

for x in depth_list:
    y = int(x)
    if z==None:
        print ("%r (First)" % y )
        z = y
    elif z > y:
        print ("%r (Down)" % y )
        z = y
    elif z < y:
        print ("%r (Up)" % y )
        z = y
        i = i+1
    else:
        print ("%r (Level)" % y )
        z = y
        j=j+1

f.close()

print(i)
