"""
Problem completed by Dylan Alexander on 02/08/2022
This problem was asked by Facebook.
Given a string of round, curly, and square open and closing brackets, 
return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false
"""

def balanced_brackets(s: str) -> bool:
	if len(s) == 1:
		return False
		
	d = {")":"(", "]":"[", "}":"{"}
	d_open = d.values()
	stack = []
	
	for i in s:
		if i in d_open:
			stack.append(i)
		elif len(stack) > 0 and stack[-1] == d[i]:
			stack.pop()
		else:
			return False
	
	return len(stack) == 0

if __name__ == "__main__":
	brackets1 = "([])[]({})"
	brackets2 = "()"
	brackets3 = "()()0"

	result1 = balanced_brackets(brackets1)
	result2 = balanced_brackets(brackets2)
	result3 = balanced_brackets(brackets3)
	print(result1,result2,result3)