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
def areBracketsBalanced(expr:str)->str:
    stack = []
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
                return char
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return char
            if current_char == '{':
                if char != "}":
                    return char
            if current_char == '[':
                if char != "]":
                    return char
            if current_char == '<':
                if char != ">":
                    return char
    # Check Empty Stack
    if stack:
        return "Incomplete"
        
    return "Complete"


def find_corrupted_lines(list_of_strings:list) ->  int :
		list_of_instructions = list(map(lambda x : x.strip(), list_of_strings))
		
		score = 0
		
		for instr in list_of_instructions :
				response = areBracketsBalanced(instr)
				if response == ")": score += 3
				elif response == "]" : score += 57
				elif response == "}" : score += 1197
				elif response == ">" : score += 25137
		
		
		return score

def test_find_corrupted_lines() -> None :
    print(f"Corrupted lines score = {find_corrupted_lines(test_list_of_strings)}")
    print("From the script = 26397")

#test_find_low_points()
#test_find_corrupted_lines()
