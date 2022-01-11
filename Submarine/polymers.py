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
#After step 10: (1749)




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
	
def build_10_depth_dict(instr:dict) -> dict :
	lookup = dict()
	for root in instr :
		polymer = root
		for i in range(10) : 
			polymer = build_next_polymer(polymer, instr)
		lookup[root] = polymer 	
	return lookup

def double_down(instr:dict, lookup10:dict, cnt10:dict) -> dict :
	count20 = dict()
	for root in instr:
		tmp = lookup10[root]
		count20[root] = dict()
		for i in range(len(tmp)-1) :
			deep = tmp[i]+tmp[i+1]

			for char in cnt10[deep] :
				if char not in count20[root] :
					count20[root][char] = 0
				count20[root][char] += cnt10[deep][char]
				if i != len(tmp)-1 and char == tmp[i+1] :
					count20[root][char] -= 1

	return count20

def polymer_diff_max_min(list_of_strings:list, itr:int) -> int :
	polymer = list_of_strings.pop(0).strip()
	list_of_strings.pop(0) #blank line
	instr = dict()
	for string in list_of_strings :
		splt = string.split(" -> ")
		instr[splt[0]] = splt[1].strip()
		
	#polymer_compressed(polymer,instr)
	lookup10 = build_10_depth_dict(instr)
	cnt_10s = dict()
	for root in lookup10 :
		cnt_10s[root]= count_uniques(lookup10[root])
	count20 = double_down(instr, lookup10, cnt_10s)
	
	print(cnt_10s['NN'])
	print(cnt_10s['NC'])
	print(cnt_10s['CB'])

	print(count20['NN'])
	print(count20['NC'])
	print(count20['CB'])
	#print(count20['NN'])


	#NNCB

	#Dont forget to add the very last character from the polymer to the counts... 


	
	for i in range(itr):
		polymer = build_next_polymer(polymer, instr)
	
	cnt_chars = count_uniques(polymer)
	print(cnt_chars)
	
	return max(cnt_chars.values())-min(cnt_chars.values())
	
def test_polymer_diff_max_min():
	i = 20
	print(f"Diff of polymer max & min = {polymer_diff_max_min(test_list_of_strings, i)} : after {i} times")
	print("1: 7, 2: 13, 3:25, 4:49, 5:97, 10:3073")
	
test_polymer_diff_max_min()

