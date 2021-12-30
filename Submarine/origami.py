import functools as fn
import numpy as np

test_list_of_strings = [
	"6,10\n",
	"0,14\n",
	"9,10\n",
	"0,3\n",
	"10,4\n",
	"4,11\n",
	"6,0\n",
	"6,12\n",
	"4,1\n",
	"0,13\n",
	"10,12\n",
	"3,4\n",
	"3,0\n",
	"8,4\n",
	"1,10\n",
	"2,14\n",
	"8,10\n",
	"9,0\n",
	"\n",
	"fold along y=7\n",
	"fold along x=5\n"
]

class Origami :
	def __init__(self, list_of_strings:str) -> None :
		coords_list = list()
		self.fold_list = list()
		for string in list_of_strings :
			if string.find(',') != -1 :
				coords_list.append(list(map(lambda x : int(x.strip()),string.split(','))))
			elif string.find('fold along') != -1 :
				self.fold_list.append([string[11],string[13::].strip()])
		
		self.coords = np.array(coords_list)
		ndx = np.array(self.coords[:,0])
		ndy = np.array(self.coords[:,1])
		max_x = max(ndx) if max(ndx) % 2 == 0 else max(ndx)+1
		max_y = max(ndy) if max(ndy) % 2 == 0 else max(ndy)+1
		self.total_paper = np.array([[0]*(max_x+1)]*(max_y+1))
		self.total_paper[[ndy,ndx]]=1
		#print(f"Start Fold Points = {self.count_points()}")

	def print_shape(self):
		print(f"Current size x={self.total_paper.shape[1]} y={self.total_paper.shape[0]}")

	def make_fold(self, axis:str, line:int) :
		if(axis=='x'):
			left = self.total_paper[::,0:line]
			right = self.total_paper[::,line+1::]
			right = np.fliplr(right)
			self.total_paper = left+right
		else :
			top = self.total_paper[0:line,::]
			btm = self.total_paper[line+1::,::]
			btm = np.flipud(btm)
			self.total_paper = top+btm
		self.total_paper[self.total_paper>1]=1
		
	def count_points(self) -> int :
		return np.count_nonzero(self.total_paper==1)
	
	def one_fold(self):
		if len(self.fold_list) > 0 :
			self.make_fold(self.fold_list[0][0], int(self.fold_list[0][1]))
			self.fold_list.pop(0)
	
	def all_folds(self):
		for fold in self.fold_list :
			self.make_fold(fold[0], int(fold[1]))
	
	def print_code(self):
		for y in self.total_paper:
			print(fn.reduce(lambda string, char: string + ("#" if char == 1 else " "), y, ""))

def see_code(list_of_strings):
	org = Origami(list_of_strings)
	org.all_folds()
	org.print_code()

def count_fold_points(list_of_strings, one_fold:bool) -> int :
	org = Origami(list_of_strings)
	if one_fold :
		org.one_fold()
	else :
		org.all_folds()
	return org.count_points()

def test_count_fold_points() -> None:
	print(f"Count of points after 1 fold = {count_fold_points(test_list_of_strings, True)}")
	print("From the script = 17 after 1")

def test_see_code() -> None:
	see_code(test_list_of_strings)
	print("From the script O")

#test_see_code()
#test_count_fold_points()

