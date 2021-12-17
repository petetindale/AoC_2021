import functools as fn


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
    
    def __str__(self) -> str:
        return str(f"x = {self.x}, y = {self.y}")


    def from_xy(self, x:int, y:int):
        self.x = x
        self.y = y
        return self

    def from_string(self, coordinate_string:str):
        list_of_xy = list(map(int, coordinate_string.split(",")))
        self.x = list_of_xy[0]
        self.y = list_of_xy[1]
        return self
    
def simple_line(pos1:Coordinate, pos2:Coordinate) -> list:
    list_of_coords = list()
    list_of_coords.append(pos1)
    if pos1 != pos2 :
        dx = pos2.x - pos1.x
        dy = pos2.y - pos1.y
        current = 0
        if dx != 0 :
            while current != dx :
                current = current + (1 if dx > 0 else -1)
                list_of_coords.append(Coordinate().from_xy(pos1.x+current, pos1.y))
        elif dy != 0 :
            while current != dy :
                current = current + (1 if dy > 0 else -1)
                list_of_coords.append(Coordinate().from_xy(pos1.x, pos1.y+current))
    return list_of_coords

def bresenham_line_generator(pos1:Coordinate, pos2:Coordinate) -> list :
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
    def __init__(self, direction_string:str) -> None:
        list_of_coordinates = list(map(lambda x : Coordinate().from_string(x), direction_string.strip().split(" -> ")))
        self.first = list_of_coordinates[0]
        self.last = list_of_coordinates[1]
        pass
    def is_horizontal_or_vertical(self) -> bool:
        return (self.first.x == self.last.x or self.first.y == self.last.y)
    def get_list_of_coordinates_between_points(self) -> list:
        list_of_coordinates = list()
        if self.is_horizontal_or_vertical() :
            list_of_coordinates = simple_line(self.first, self.last)
        else :
            list_of_coordinates = bresenham_line_generator(self.first, self.last)
        return list_of_coordinates

        

    

class Geo_Map :
    def __init__(self, size:int) -> None:
        self.size = size
        self.geo_points = [[0] * size for y in range(size)]
        pass
    def add_vent_mapping(self, vent_map) :
        for coords in vent_map :
            self.geo_points[coords.y][coords.x] += 1
    def count_overlapping_vents(self) :
        return int(fn.reduce(lambda count, ls: count+int(fn.reduce(lambda cnt2, overlaps: cnt2 + (1 if overlaps > 1 else 0), ls, 0)),self.geo_points, 0))
    def __str__(self) -> str:
        str  = ""
        for ls in self.geo_points :
            line = fn.reduce(lambda string, item: f"{string}{item}" if item > 0 else f"{string}.", ls, "")
            str = f"{str}{line}\n"
        return str



def find_overlapping_vents(list_of_strings:list, only_horizontal_or_vertical:bool, map_size:int) -> int:
    list_of_vent_maps = list(map(lambda x : Vent_Mapping(x), list_of_strings))
    geo_map = Geo_Map(map_size)
    if only_horizontal_or_vertical :
        list_of_vent_maps = list(filter(lambda x : x.is_horizontal_or_vertical(), list_of_vent_maps))
    for vent_map in list_of_vent_maps :
        geo_map.add_vent_mapping((vent_map.get_list_of_coordinates_between_points()))
    overlapping_vents = geo_map.count_overlapping_vents()
    #716,934
    #print(geo_map)
    return overlapping_vents

def test_find_overlapping_vents() :
    print(f"There are {find_overlapping_vents(test_list_of_strings, False, 10)} vents.")

#test_find_overlapping_vents()