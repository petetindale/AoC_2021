#from multiprocessing import parent_process
from copy import copy, deepcopy
import functools
from typing import Tuple

test_list_of_strings = [
	"[1,2]\n"
	,"[[1,2],3]\n"
	,"[9,[8,7]]\n"
	,"[[1,9],[8,5]]\n"
	,"[[[[1,2],[3,4]],[[5,6],[7,8]]],9]\n"
	,"[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]\n"
	,"[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]\n"
	,"[[[[[9,8],1],2],3],4]\n"
	,"[[1,2],[[3,4],5]]\n"
]

test_expanded_list_of_strings = [
	"[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]\n"
	,"[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]\n"
	,"[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]\n"
	,"[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]\n"
	,"[7,[5,[[3,8],[1,4]]]]\n"
	,"[[2,[2,2]],[8,[8,1]]]\n"
	,"[2,9]\n"
	,"[1,[[[9,3],9],[[9,0],[0,7]]]]\n"
	,"[[[5,[7,4]],7],1]\n"
	,"[[[[4,2],2],6],[8,7]]\n"
]

test_homework_list_of_strings = [
	"[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]\n"
	,"[[[5,[2,8]],4],[5,[[9,9],0]]]\n"
	,"[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]\n"
	,"[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]\n"
	,"[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]\n"
	,"[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]\n"
	,"[[[[5,4],[7,7]],8],[[8,3],8]]\n"
	,"[[9,3],[[9,9],[6,[4,9]]]]\n"
	,"[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]\n"
	,"[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]\n"
]

def matchedbrackets(brackets:str)->str:
	count = 0
	build = ''
	for char in brackets:
		if char == '[' :
			count += 1
		elif char == ']':
			count -= 1
		build += char
		if count==0 :
			return build
	return ''
	

class Pair:
	def __init__(self, parent=None)->None:
		self.value:int = -1
		self.left:Pair = None
		self.right:Pair = None
		self.parent:Pair = parent
		pass
		
	def isvalue(self)->bool:
		return self.value != -1 

	def haschildren(self)->bool:
		if self.isvalue() :
			return False
		elif self.left.isvalue() and self.right.isvalue() :
			return False
		return True
	
	def getmagnitude(self)->int:
		if self.isvalue():
			return self.value
		return self.left.getmagnitude()*3 + self.right.getmagnitude()*2

	def checkdepthrule(self,depth:int=1)->Tuple[bool,'Pair']:
		if not self.isvalue():
			if depth > 4:
				if self.haschildren():
					print('error')
				#print(f'explode {self} at {depth}')
				return (True,self)
			depth += 1
			leftfound, left = self.left.checkdepthrule(depth)
			if not leftfound :
				return self.right.checkdepthrule(depth)
			return (True, left)
		return (False,None)

	def applyrules(self)->'Pair':
		rules = True
		while rules:
			depth = self.applydepthrule()
			value = False
			if not depth:
				value = self.applyvaluerule()
			rules = depth or value
		return self

	def applyvaluerule(self)->bool:
		if self.isvalue():
			if self.value > 9:
				i = self.value
				r = i % 2
				i = int((i - r)/2)

				self.left = Pair(self)	
				self.right = Pair(self)
				self.value = -1

				self.left.value = i
				self.right.value = i + r
				return True
			return False
		else :
			if not self.left.applyvaluerule():
				return self.right.applyvaluerule()
			else:
				return True

	def applydepthrule(self)->bool:
		found, pair = self.checkdepthrule()
		if found and not pair.haschildren():
				lvalue = None
				rvalue = None
				lfound,lpair = pair.parent.findleftvalueof(pair)
				rfound,rpair = pair.parent.findrightvalueof(pair)
				
				if pair.parent.left == pair:
					side = 'left'
				else:
					side = 'right'

				if lfound:
					lvalue = lpair.getvaluepair('right')
					lvalue.value += pair.left.value
					
				if rfound:
					rvalue = rpair.getvaluepair('left')
					rvalue.value += pair.right.value
				
				zero = Pair(pair.parent)
				zero.value = 0

				if side == 'left':
					pair.parent.left = zero
				else:
					pair.parent.right = zero

		return found	


	def findleftvalueof(self, prev:'Pair')->Tuple[bool,'Pair']:
		if prev == self.left:
			if self.parent == None:
				return (False, None)
			else:
				return self.parent.findleftvalueof(self)
		else:
			return (True,self.left)
	
	def findrightvalueof(self, prev:'Pair')->Tuple[bool,'Pair']:
		if prev == self.right:
			if self.parent == None:
				return (False, None)
			else:
				return self.parent.findrightvalueof(self)
		else:
			return (True,self.right)
	
	def getvaluepair(self, dir:str)->'Pair':
		if self.isvalue():
			return self
		elif dir == 'left':
			return self.left.getvaluepair('left')
		elif dir == 'right':
			return self.right.getvaluepair('right')
		else:
			return None


	def __str__(self)->str:
		if self.isvalue():
			return f'{self.value}'
		return f'[{self.left},{self.right}]'

	@classmethod
	def add_pair(cls, left:'Pair', right:'Pair')->'Pair':
		if left == None:
			return right
		pair = Pair()
		pair.left = deepcopy(left)
		pair.right = deepcopy(right)

		pair.left.parent = pair
		pair.right.parent = pair

		return pair

	@classmethod
	def pair_fromstr(cls, pairstr:str, parent:'Pair'=None)->'Pair':
			pair = Pair(parent)
			if pairstr.isnumeric() :
				pair.value = int(pairstr)
			else :
				middle = 0
				if pairstr[1].isnumeric():
					end = pairstr.find(',')
					pair.left = Pair.pair_fromstr(pairstr[1:end],pair)
					
					middle = end+1
				else :
					lpair = matchedbrackets(pairstr[1:-1])
					middle = len(lpair)+2
					pair.left = Pair.pair_fromstr(lpair,pair)
				if pairstr[-2].isnumeric() :
					start = pairstr.rfind(',')+1
					pair.right = Pair.pair_fromstr(pairstr[start:-1],pair)
				else :
					rpair = matchedbrackets(pairstr[middle:-1])
					pair.right = Pair.pair_fromstr(rpair,pair)
			return pair


def find_max_magnitude(list_of_strings:list)->int:
	list_of_pairs = list(map(lambda x:Pair.pair_fromstr(x.strip()),list_of_strings))

	max_magnitude = 0

	for leftpair in list_of_pairs:
		for rightpair in list_of_pairs:
			if leftpair != rightpair:
				max_magnitude = max(Pair.add_pair(leftpair,rightpair).applyrules().getmagnitude(), max_magnitude)

	return max_magnitude



def final_sum_magnitude(list_of_strings:list)->int:
	list_of_pairs = list(map(lambda x:Pair.pair_fromstr(x.strip()),list_of_strings))
	print('======================')
	for p in list_of_pairs: print(p)
	x = functools.reduce(lambda sum, pair: Pair.add_pair(sum, pair).applyrules(), list_of_pairs)
	print('----------------------')
	print(x)
	print('======================')
	return x.getmagnitude()

def test_final_sum_magnitude()->None:
	print(f'TEST - Final Sum Magnitude = {final_sum_magnitude(test_homework_list_of_strings)}')
	print('ASSERT - FSM = 4140')

def test_find_max_magnitude()->None:
	print(f'TEST - Find Max Sum = {find_max_magnitude(test_homework_list_of_strings)}')
	print('ASSERT - FMM = 3993')

#test_find_max_magnitude()
#test_final_sum_magnitude()
