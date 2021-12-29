import functools as fn
import numpy as np

test_list_of_strings_tiny = [
	"start-A\n",
	"start-b\n",
	"A-b\n",
	"A-end\n",
	"b-end\n"
]

test_list_of_strings_simple = [
	"start-A\n",
	"start-b\n",
	"A-c\n",
	"A-b\n",
	"b-d\n",
	"A-end\n",
	"b-end\n"
]

test_list_of_strings_medium = [
	"dc-end",
	"HN-start",
	"start-kj",
	"dc-start",
	"dc-HN",
	"LN-dc",
	"HN-end",
	"kj-sa",
	"kj-HN",
	"kj-dc"
]

test_list_of_strings_complex = [
	"fs-end",
	"he-DX",
	"fs-he",
	"start-DX",
	"pj-DX",
	"end-zg",
	"zg-sl",
	"zg-pj",
	"pj-he",
	"RW-he",
	"fs-DX",
	"pj-RW",
	"zg-RW",
	"start-pj",
	"he-WI",
	"zg-he",
	"pj-fs",
	"start-RW"
]

class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = dict()
        self._graph_dict = graph_dict

    def edges(self, vertice):
        """ returns a list of all the edges of a vertice"""
        return self._graph_dict[vertice]
        
    def all_vertices(self):
        """ returns the vertices of a graph as a set """
        return set(self._graph_dict.keys())

    def all_edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self._graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graph_dict:
                self._graph_dict[x].append(y)
            else:
                self._graph_dict[x] = [y]

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self._graph_dict:
            for neighbour in self._graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
    
    def __iter__(self):
        self._iter_obj = iter(self._graph_dict)
        return self._iter_obj
    
    def __next__(self):
        """ allows us to iterate over the vertices """
        return next(self._iter_obj)

    def __str__(self):
        res = "vertices: "
        for k in self._graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

class Cave_System :
	def __init__(self, list_of_strings):
		self.graph = Graph()
		for string in list_of_strings :
			self.graph.add_edge(set(string.strip().split("-")))
		
	def get_small_caves(self):
		return list(filter(lambda cv : cv.islower() and cv not in ['start','end'], self.graph.all_vertices()))
	
	def traverse_caves(self, cave:str, current_depth, max_depth, small_cave_visit, all_routes:list, traversed:list=list()):
		if current_depth > max_depth : return 
		
		if ((cave in ['start','end'] and cave not in traversed) or (cave == small_cave_visit and traversed.count(small_cave_visit)<2) or (cave not in ['start','end'] and cave.islower() and cave not in traversed) or cave.isupper()) :
			traversed.append(cave)
			if cave == 'end' : 
				all_routes.append(str(traversed))
				traversed.pop()
				return 
				
			for nextCave in self.graph.edges(cave):
				self.traverse_caves(nextCave, current_depth+1, max_depth, small_cave_visit, all_routes, traversed)
				
			traversed.pop()
		return
		

def count_small_cave_paths(list_of_strings:str) -> int :
	cv = Cave_System(list_of_strings)
	all_routes = list()
	'''this is proper nasty - could be done much cleaner than iteration'''
	for sm in cv.get_small_caves():
		cv.traverse_caves('start', 0, 100, sm, all_routes)
	all_routes = set(all_routes)
	return len(all_routes)

def test_count_small_cave_paths() -> None:
	print(f"Small cave visit simple = {count_small_cave_paths(test_list_of_strings_simple)}")
	print("From the script = simple - 10")
	print(f"Small cave visit medium = {count_small_cave_paths(test_list_of_strings_medium)}")
	print("From the script = medium - 19")
	print(f"Small cave visit complex = {count_small_cave_paths(test_list_of_strings_complex)}")
	print("From the script = complex - 226")


#test_count_small_cave_paths()
