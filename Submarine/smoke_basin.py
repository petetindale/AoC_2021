import functools as fn
import numpy as np

test_list_of_strings = ["2199943210\n",
    "3987894921\n",
    "9856789892\n",
    "8767896789\n",
    "9899965678\n"]

def find_low_points(list_of_strings:list) -> int :
    depth_map = np.array(list(map(lambda rows : list(map(lambda chars: int(chars), rows.strip())), list_of_strings)), np.short)
    low_points = list()
    for y in range(depth_map.shape[0]) :
        for x in range(depth_map.shape[1]) :
            if y > 0 : top = depth_map[y-1, x] 
            else : top = 10

            if y < depth_map.shape[0]-1 : bottom = depth_map[y+1, x]  
            else : bottom = 10

            if x > 0 : left = depth_map[y, x-1]  
            else : left = 10

            if x < depth_map.shape[1]-1 : right = depth_map[y, x+1]  
            else : right = 10

            if depth_map[y , x] < top \
                and depth_map[y , x] < bottom \
                and depth_map[y , x] < left \
                and depth_map[y , x] < right :
                low_points.append(depth_map[y , x])

    print(len(low_points))
    print(depth_map.shape)
    return sum(list(map(lambda lp : lp+1, low_points)))

def find_largest_basins(list_of_strings:list) -> int :
    depth_map = np.array(list(map(lambda rows : list(map(lambda chars: int(chars), rows.strip())), list_of_strings)), np.short)
    contour_map = np.zeros_like(depth_map,np.short)


    low_points = list()
    for y in range(depth_map.shape[0]) :
        for x in range(depth_map.shape[1]) :
            if y > 0 : top = depth_map[y-1, x] 
            else : top = 10

            if y < depth_map.shape[0]-1 : bottom = depth_map[y+1, x]  
            else : bottom = 10

            if x > 0 : left = depth_map[y, x-1]  
            else : left = 10

            if x < depth_map.shape[1]-1 : right = depth_map[y, x+1]  
            else : right = 10

            if depth_map[y , x] < top \
                and depth_map[y , x] < bottom \
                and depth_map[y , x] < left \
                and depth_map[y , x] < right :
                low_points.append(depth_map[y , x])

    print(len(low_points))
    print(depth_map.shape)
    return sum(list(map(lambda lp : lp+1, low_points)))

def test_find_low_points() -> None :
    print(f"Sum of Risk Level = {find_low_points(test_list_of_strings)}")
    print("From the script = 15")

def test_find_largest_basins() -> None :
    print(f"Product of 3 largest basins = {find_largest_basins(test_list_of_strings)}")
    print("From the script = 1134")

#test_find_low_points()
test_find_largest_basins()