from typing import Tuple, Iterator, Optional, TypeVar
import numpy as np

# Borrows from here...
# Sample code from https://www.redblobgames.com/pathfinding/a-star/
# Copyright 2014 Red Blob Games <redblobgames@gmail.com>

test_list_of_strings = [
	"1163751742\n",
	"1381373672\n",
	"2136511328\n",
	"3694931569\n",
	"7463417111\n",
	"1319128137\n",
	"1359912421\n",
	"3125421639\n",
	"1293138521\n",
	"2311944581\n"
]

T = TypeVar('T')
GridLocation = Tuple[int,int]

def expand_grid(weights:np.array) -> np.array:
	seed = np.copy(weights)
	next = np.copy(weights)
	for i in range(4):	
		next += 1
		next[next>9]=1
		seed = np.concatenate((seed,next),0)
	next = np.copy(seed)
	for i in range(4):	
		next += 1
		next[next>9]=1
		seed = np.concatenate((seed,next),1)
	return seed



class Grid:
	def __init__(self, list_of_strings:str, expanded_grid:bool=False) -> None:
		self.weights = np.array(list(map(lambda rows : list(map(lambda chars: int(chars), rows.strip())), list_of_strings)), int)
		if expanded_grid :
			self.weights = expand_grid(self.weights)
		self.height = self.weights.shape[0]
		self.width = self.weights.shape[1]
		self.top_left = (0,0)
		self.bottom_right = (self.width-1,self.height-1)
	
	def in_bounds(self, id: GridLocation) -> bool:
		(x , y) = id
		return 0 <= x < self.width and 0 <= y < self.height
	
	def neighbors(self, id: GridLocation) -> Iterator[GridLocation]:
		(x, y) = id
		neighbors = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)] # E W N S
		# see "Ugly paths" section for an explanation:
		if (x + y) % 2 == 0: neighbors.reverse() # S N W E
		results = filter(self.in_bounds, neighbors)
		return results
	
	def cost(self, from_node: GridLocation, to_node: GridLocation) -> int:
		(x,y) = to_node
		return self.weights[y,x]

import heapq

class PriorityQueue:
    def __init__(self):
        self.elements: list[tuple[int, T]] = []
    
    def empty(self) -> bool:
        return not self.elements
    
    def put(self, item: T, priority: int):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self) -> T:
        return heapq.heappop(self.elements)[1]

def heuristic(a: GridLocation, b: GridLocation) -> int:
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(graph: Grid, start: GridLocation, goal: GridLocation):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from: dict[GridLocation, Optional[GridLocation]] = {}
    cost_so_far: dict[GridLocation, int] = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current: GridLocation = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far


def find_route(list_of_strings:str, expanded_grid:bool=False) -> int :
	grid = Grid(list_of_strings, expanded_grid)
	came_from, cost_so_far = a_star_search(grid, grid.top_left, grid.bottom_right)
	return cost_so_far[grid.bottom_right]

def test_find_route() :
	print("Route finding - Test")
	print(f"Test result {find_route(test_list_of_strings, True)}")
	print("Expected - 40 or 315 for expanded")

test_find_route()