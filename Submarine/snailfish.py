#from multiprocessing import parent_process


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
	
	def applydepthrule(self,depth:int=1)->bool:
		if not self.isvalue():
			if depth > 4:
				if self.haschildren():
					print('error')
				print(f'explode {self} at {depth}')
				return True
			depth += 1
			if not self.left.applydepthrule(depth):
				return self.right.applydepthrule(depth)
			return True
		return False

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
			
		
	def isvalue(self)->bool:
		return self.value != -1 

	def haschildren(self)->bool:
		if self.isvalue() :
			return False
		elif self.left.isvalue() and self.right.isvalue() :
			return False
		return True

	def findleftvalue(self)->'Pair':
		return self.parent.left
    
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
		p.applydepthrule()
		p.applyvaluerule()
		
		p = Pair.add_pair(p, Pair.pair_fromstr('[2,1]'))
		
		print(p)
		p.applydepthrule()
		p.applyvaluerule()
		
		
	return 0

def test_final_sum_magnitude()->None:
	print(f'TEST - Final Sum Magnitude = {final_sum_magnitude(test_list_of_strings)}')
	print('ASSERT - FSM = 4140')

test_final_sum_magnitude()
