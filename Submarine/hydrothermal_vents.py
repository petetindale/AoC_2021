

from typing import Coroutine


test_list_of_strings = ["0,9 -> 5,9\n",
   "8,0 -> 0,8\n",
   "9,4 -> 3,4\n",
   "2,2 -> 2,1\n",
   "7,0 -> 7,4\n",
   "6,4 -> 2,0\n",
   "0,9 -> 2,9\n",
   "3,4 -> 1,4\n",
   "0,0 -> 8,8\n",
   "5,5 -> 8,2\n"]

test_overalps = 5



class Coordinate :
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
    
    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y

    def __ne__(self, __o: object) -> bool:
        return not(self.x == __o.x and self.y == __o.y)

    def from_xy(self, x:int, y:int):
        self.x = x
        self.y = y
        return self

    def from_string(self, coordinate_string):
        list_of_xy = list(map(int, coordinate_string.split(",")))
        self.x = list_of_xy[0]
        self.y = list_of_xy[1]
        return self
    
def simple_line(pos1:Coordinate, pos2:Coordinate) -> list:
    list_of_coords = list()
    list_of_coords.append(pos1)
    if pos1 != pos2 :
        list_of_coords.append(pos2)
    return list_of_coords

def bresenham_line_generator(pos1, pos2) :
    x1, y1, x2, y2 = pos1.x, pos1.y, pos2.x, pos2.y
    
    x, y = x1, y1
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    gradient = dy/float(dx)

    if gradient > 1 :
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    
    p = 2 * dy - dx

    list_of_coords = list()
    list_of_coords.append(Coordinate().from_xy(x,y))
    
    for k in range(dx):
        if p > 0 :
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else :
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1

        list_of_coords.append(Coordinate().from_xy(x,y))

    return list_of_coords


class Vent_Mapping :
    def __init__(self, direction_string) -> None:
        list_of_coordinates = list(map(lambda x : Coordinate().from_string(x), direction_string.strip().split(" -> ")))
        self.first = list_of_coordinates[0]
        self.last = list_of_coordinates[1]
        pass
    def is_horizontal_or_vertical(self) -> bool:
        return (self.first.x == self.last.x or self.first.y == self.last.y)
    def get_list_of_coordinates_between_points(self) -> list:
        list_of_coordinates = list()
        if self.is_horizontal_or_vertical() :
            list_of_coordinates.append(simple_line(self.first, self.last))
        return list_of_coordinates

        

    

class Geo_Map :
    def __init__(self, size) -> None:
        self.size = size
        self.geo_points = [[0] * size for y in range(size)]
        pass
#    def add_vent_mapping(self, vent_map) :
#        vent_map. 



def find_overlapping_vents(list_of_strings, only_horizontal_or_vertical, map_size) :
    list_of_vent_maps = list(map(lambda x : Vent_Mapping(x), list_of_strings))
    geo_map = Geo_Map(map_size)
    if only_horizontal_or_vertical :
        list_of_vent_maps = list(filter(lambda x : x.is_horizontal_or_vertical(), list_of_vent_maps))
    for vent_map in list_of_vent_maps :
        vent_map.get_list_of_coordinates_between_points()
    return 0

def test_find_overlapping_vents() :
    print(f"There are {find_overlapping_vents(test_list_of_strings, True, 10)} vents.")

test_find_overlapping_vents()