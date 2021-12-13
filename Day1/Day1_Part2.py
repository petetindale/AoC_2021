from os import path

f = open(path.dirname(__file__) + "/list.txt", "r")

depth_list = f.readlines()

f.close()

depth_list = list(map(int, depth_list))

length = len(depth_list)

z = None
i=0
j=1
k=2
current3Depth = 0
last3Depth = None
up_down = ""
ups = 0
downs = 0
sames = 0

while(k<length):
    current3Depth = depth_list[i] + depth_list[j] + depth_list[k]
    
    if last3Depth == None :
        up_down = "first"
        #ignore
    elif last3Depth > current3Depth :
        up_down = "down"
        downs += 1
    elif last3Depth < current3Depth :
        up_down = "up"
        ups += 1
    else :
        up_down = "same"
        sames += 1

    
    print(" %r, %r, %r = [%r] - %s" % (depth_list[i], depth_list[j], depth_list[k], current3Depth, up_down)) 
    i += 1
    j += 1
    k += 1
    last3Depth = current3Depth



print("Ups %r, Downs %r, Sames %r" % (ups, downs, sames))
