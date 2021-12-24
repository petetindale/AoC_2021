import functools as fn
import numpy as np

test_list_of_strings = ["2199943210\n",
    "3987894921\n",
    "9856789892\n",
    "8767896789\n",
    "9899965678\n"]

def initialise_depth_map(list_of_strings:list) -> np.array :
		return np.array(list(map(lambda rows : list(map(lambda chars: int(chars), rows.strip())), list_of_strings)), np.short)

def find_low_points(list_of_strings:list) -> int :
    depth_map = initialise_depth_map(list_of_strings)
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
    

def fill_contour_map(contour_map:np.array, basin_count:list, y:int, x:int, fill:int) -> None :

		if y < 0 or y >= contour_map.shape[0] or x < 0 or x >= contour_map.shape[1] : return 
		elif contour_map [y , x] != 0 : return 
		else :
				contour_map [y , x] = fill
				if len(basin_count) < fill+1:
						basin_count.append(1)
				else :
						basin_count[fill] += 1
				fill_contour_map(contour_map, basin_count, y-1, x, fill)
				fill_contour_map(contour_map, basin_count, y+1, x, fill)
				fill_contour_map(contour_map, basin_count, y, x-1, fill)
				fill_contour_map(contour_map, basin_count, y, x+1, fill)
				
		pass

def find_largest_basins(list_of_strings:list) -> int :
    depth_map = initialise_depth_map(list_of_strings)
    contour_map = np.zeros_like(depth_map,np.short)

    
    #print(depth_map)
    I,J = np.where(depth_map==9)
    for a in range(len(I)) :
    		contour_map[I[a], J[a]] = -1
    
    basin_count = list()
    basin_count.append(0)
    current_basin = 1
    
    while np.count_nonzero(contour_map==0) != 0 :
    		Y,X = np.where(contour_map==0)
    		fill_contour_map(contour_map, basin_count, Y[0], X[0], current_basin)
    		current_basin += 1
    
    #print(contour_map)
    
    basin_count.sort(reverse=True)
    
    prd_3_largest_basins = 0
    if len(basin_count) > 3 :
    	prd_3_largest_basins = basin_count[0]*basin_count[1]*basin_count[2]
    #print(basin_count)

    return prd_3_largest_basins

def test_find_low_points() -> None :
    print(f"Sum of Risk Level = {find_low_points(test_list_of_strings)}")
    print("From the script = 15")

def test_find_largest_basins() -> None :
    print(f"Product of 3 largest basins = {find_largest_basins(test_list_of_strings)}")
    print("From the script = 1134")

#test_find_low_points()
test_find_largest_basins()
