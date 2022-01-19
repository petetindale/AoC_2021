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
	

class SFPair:
	def __init__(self, parent=None)->None:
		self.value:int = -1
		self.left:SFPair = None
		self.right:SFPair = None
		self.parent:SFPair = parent
		#self.depth = 0
		pass
	
	def checkdepthrule(self,depth:int=0)->int:
		if self.value != -1:
			if depth > 4:
				print('explode')
			return depth
		depth += 1
		ldepth = self.left.checkdepthrule(depth)
		rdepth = self.right.checkdepthrule(depth)
		return max(ldepth,rdepth)
		

	def __str__(self)->str:
		if self.value != -1:
			return f'{self.value}'
		return f'[{self.left},{self.right}]'

def pair_fromstr(pairstr:str, parent:SFPair=None)->SFPair:
		pair = SFPair(parent)
		if pairstr.isnumeric() :
			pair.value = int(pairstr)
		else :
			middle = 0
			if pairstr[1].isnumeric():
				end = pairstr.find(',')
				pair.left = pair_fromstr(pairstr[1:end],pair)
				
				middle = end+1
			else :
				lpair = matchedbrackets(pairstr[1:-1])
				middle = len(lpair)+2
				pair.left:SFPair = pair_fromstr(lpair,pair)
			if pairstr[-2].isnumeric() :
				start = pairstr.rfind(',')+1
				pair.right = pair_fromstr(pairstr[start:-1],pair)
			else :
				rpair = matchedbrackets(pairstr[middle:-1])
				pair.right:SFPair = pair_fromstr(rpair,pair)
		return pair

def final_sum_magnitude(list_of_strings:list)->int:
	list_of_pairs = list(map(lambda x:pair_fromstr(x.strip()),list_of_strings))
	for p in list_of_pairs:
		print(p.checkdepthrule())
	return 0

def test_final_sum_magnitude()->None:
    print(f'TEST - Final Sum Magnitude = {final_sum_magnitude(test_list_of_strings)}')
    print('ASSERT - FSM = 4140')

test_final_sum_magnitude()
