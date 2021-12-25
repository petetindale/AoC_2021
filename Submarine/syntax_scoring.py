import functools as fn
import numpy as np

test_list_of_strings = ["[({(<(())[]>[[{[]{<()<>>\n",
		"[(()[<>])]({[<{<<[]>>(\n",
		"{([(<{}[<>[]}>{[]{[(<()>\n",
		"(((({<>}<{<{<>}{[]{[]{}\n",
		"[[<[([]))<([[{}[[()]]]\n",
		"[{[{({}]{}}([{[{{{}}([]\n",
		"{<[[]]>}<{[{[{[]{()[[[]\n",
		"[<(<(<(<{}))><([]([]()\n",
		"<{([([[(<>()){}]>(<<{{\n",
		"<{([{{}}[<[[[<>{}]]]>[]]\n"]

#): 3 points.
#]: 57 points.
#}: 1197 points.
#>: 25137 points.

#Borrowed with pride from https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
def areBracketsBalanced(expr:str, return_incomplete:bool):
    stack = []
    resp = []
    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "[", "<"]:
            # Push the element in the stack
            stack.append(char)
        else:
            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return [char]
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                		resp.append(char)
                		return resp if not return_incomplete else []
            if current_char == '{':
                if char != "}":
                		resp.append(char)
                		return resp if not return_incomplete else []
            if current_char == '[':
                if char != "]":
                		resp.append(char)
                		return resp if not return_incomplete else []
            if current_char == '<':
                if char != ">":
                		resp.append(char)
                		return resp if not return_incomplete else []
    # Check Empty Stack
    if stack:
        return stack if return_incomplete else []
        
    return resp


def find_corrupted_lines(list_of_strings:list) ->  int :
		list_of_instructions = list(map(lambda x : x.strip(), list_of_strings))
		
		score = 0
		
		for instr in list_of_instructions :
				response = areBracketsBalanced(instr,False)
				if len(response) == 1 :
						if response[0] == ")": score += 3
						elif response[0] == "]" : score += 57
						elif response[0] == "}" : score += 1197
						elif response[0] == ">" : score += 25137
		
		
		return score

def complete_lines(list_of_strings:list) ->  int :
		list_of_instructions = list(map(lambda x : x.strip(), list_of_strings))
		
		score_list = []
		
		for instr in list_of_instructions :
				response = areBracketsBalanced(instr,True)
				
				if response != [] :
						response.reverse()
						score = 0
						for char in response :
								score = score * 5
								if char == "(" : score += 1
								elif char == "[" : score += 2
								elif char == "{" : score += 3
								elif char == "<" : score += 4
						score_list.append(score)
					
		return int(np.median(score_list))

def test_find_corrupted_lines() -> None :
    print(f"Corrupted lines score = {find_corrupted_lines(test_list_of_strings)}")
    print("From the script = 26397")

def test_complete_lines() -> None :
    print(f"Incomplete lines score = {complete_lines(test_list_of_strings)}")
    print("From the script = 288957")


#test_find_low_points()
#test_find_corrupted_lines()
#test_complete_lines()
