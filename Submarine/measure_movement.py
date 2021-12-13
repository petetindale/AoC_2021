import functools

def measure_depth(list_of_strings):
    z = None
    i=0
    j=0

    for x in list_of_strings:
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

    return i


def measure_threes_depth(list_of_strings):
    depth_list = list(map(int, list_of_strings))

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
    return ups