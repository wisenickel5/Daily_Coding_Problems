"""
Problem completed by Dylan Alexander on 02/08/2022
This problem was asked by Facebook.
Given a string of round, curly, and square open and closing brackets, 
return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false
"""

def balanced_brackets(s: str) -> bool:
    if len(s) == 0:
        return True

if __name__ == "__main__":
    brackets = "([])[]({})"
    result = balanced_brackets(brackets)
    print(result)