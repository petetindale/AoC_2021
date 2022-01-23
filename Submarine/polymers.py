test_list_of_strings = [
	"NNCB\n",
	"\n",
	"CH -> B\n",
	"HH -> N\n",
	"CB -> H\n",
	"NH -> C\n",
	"HB -> C\n",
	"HC -> B\n",
	"HN -> C\n",
	"NN -> C\n",
	"BH -> H\n",
	"NC -> B\n",
	"NB -> B\n",
	"BN -> B\n",
	"BB -> N\n",
	"BC -> B\n",
	"CC -> N\n",
	"CN -> C\n"
]

#After step 1: NCNBCHB (7)
#After step 2: NBCCNBBBCBHCB (13)
#After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB (25)
#After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB (49)
#After step 5: (97)
#After step 10: (1588)




def list_from_polymer(polymer:str) -> list :
	poly_len = len(polymer)
	poly_list = list()
	for i in range(poly_len-1) :
		poly_list.append([polymer[i]+polymer[i+1],0])
	return poly_list

def polymer_compressed(polymer:str, instr:dict) -> str :
	lp = list_from_polymer(polymer)
	cmpr_dict = dict()
	for poly_seed in lp :
		if poly_seed[0] not in cmpr_dict : 
			cmpr_dict[poly_seed[0]] = [poly_seed]
		else : 
			cmpr_dict[poly_seed[0]].append(poly_seed)
	print(cmpr_dict)

def polymer_get_roots(root, depth, instr, cmpr_dict):
	if root not in cmpr_dict :
		cmpr_dict[root]=list([[root,0]])
	if len(cmpr_dict[root])<depth:
		for i in range(depth):
			if i not in cmpr_dict[root]:
				poly_ins = instr[root]
				left = root[0]+poly_ins
				right = poly_ins+root[1]
				cmpr_dict[root].append([[left,0],[right,0]])
		#cmpr_dict[root][i+1] = cmpr_dict[root]

def build_next_polymer(polymer:str, instr:dict) -> str :
	polymer_new = ''
	for i in range(len(polymer)-1) :
		polymer_new += polymer[i] + instr[polymer[i]+polymer[i+1]]
	polymer_new += polymer[-1]
	return polymer_new

def count_uniques(polymer:str) -> dict :
	set_plymr = set(polymer)
	cnt_plymr = dict()
	for char in set_plymr :
		cnt_plymr[char] = polymer.count(char)
		#print(f"char - {char} : {cnt_plymr[char]}")
	return cnt_plymr
	
def build_depth_dict(instr:dict, depth:int) -> dict :
	lookup = dict()
	for root in instr :
		polymer = root
		for i in range(depth) : 
			polymer = build_next_polymer(polymer, instr)
		lookup[root] = polymer 	
	return lookup
	
def count_from_counts(polymer:str, counts:dict,inc_last:bool=False)->dict:
	tmp = polymer
	new_count = dict()
	for i in range(len(tmp)-1) :
		deep = tmp[i]+tmp[i+1]

		for char in counts[deep] :
			if char not in new_count :
				new_count[char] = 0
			new_count[char] += counts[deep][char]
			if i != len(tmp)-1 and char == tmp[i+1] :
				new_count[char] -= 1
		if inc_last and i != 0: 
			new_count[tmp[i]] += 1
	if inc_last :
		new_count[tmp[-1]]+=2

	return new_count

def double_down(instr:dict, lookup:dict, counts:dict) -> dict :
	countdouble = dict()
	for root in instr:
		countdouble[root]= count_from_counts(lookup[root],counts)
	return countdouble

def polymer_diff_max_min(list_of_strings:list, itr:int) -> int :
	polymer = list_of_strings.pop(0).strip()
	list_of_strings.pop(0) #blank line
	instr = dict()
	for string in list_of_strings :
		splt = string.split(" -> ")
		instr[splt[0]] = splt[1].strip()
	
	#this really isn't the cleverest or cleanest way of doing this. but it got there
		
	#polymer_compressed(polymer,instr)
	lookup = build_depth_dict(instr,15)
	counts = dict()
	for root in lookup :
		counts[root]= count_uniques(lookup[root])
	countdouble = double_down(instr, lookup, counts)
	
	print(count_from_counts(polymer,countdouble, True))


	#NNCB

	#Dont forget to add the very last character from the polymer to the counts... 


	
	for i in range(itr):
		polymer = build_next_polymer(polymer, instr)
	
	cnt_chars = count_from_counts(polymer,countdouble,True)
	print(count_uniques(polymer))
	print(cnt_chars)
	
	return max(cnt_chars.values())-min(cnt_chars.values())
	
def test_polymer_diff_max_min():
	i = 10
	print(f"Diff of polymer max & min = {polymer_diff_max_min(test_list_of_strings, i)} : after {i} times")
	print("1: 7, 2: 13, 3:25, 4:49, 5:97, 10:3073")
	
#test_polymer_diff_max_min()

