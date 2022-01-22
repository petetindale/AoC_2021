#from multiprocessing import parent_process
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

	def checkdepthrule(self,depth:int=1)->Tuple[bool,'Pair']:
		if not self.isvalue():
			if depth > 4:
				if self.haschildren():
					print('error')
				print(f'explode {self} at {depth}')
				return (True,self)
			depth += 1
			leftfound, left = self.left.checkdepthrule(depth)
			if not leftfound :
				return self.right.checkdepthrule(depth)
			return (True, left)
		return (False,None)

	def applyrules(self)->None:
		rules = True
		while rules:
			depth = self.applydepthrule()
			value = self.applyvaluerule()
			rules = depth or value

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
		pair = Pair()
		pair.left = left
		pair.right = right

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

def final_sum_magnitude(list_of_strings:list)->int:
	list_of_pairs = list(map(lambda x:Pair.pair_fromstr(x.strip()),list_of_strings))
	for p in list_of_pairs:
		print('================')
		
		print(p)
		p.applyrules()
		print(p)
		
		p = Pair.add_pair(p, Pair.pair_fromstr('[[[[2,1],1],2],3]'))
		
		print(p)
		p.applyrules()
		print(p)
		
		
	return 0

def test_final_sum_magnitude()->None:
	print(f'TEST - Final Sum Magnitude = {final_sum_magnitude(test_list_of_strings)}')
	print('ASSERT - FSM = 4140')

test_final_sum_magnitude()
