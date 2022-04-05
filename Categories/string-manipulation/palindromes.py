'''
Completed by Dylan Alexander on 04/04/2022
A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads 
the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
'''

def is_palindrome(s: str) -> bool:
	shortend = [i for i in s if (i.isalnum()) == True]
	new_word = "".join(shortend)
	comp_list = []
	for i in range(len(s) - 1, -1, -1):
		if s[i].isalnum() == True:            
			comp_list.append(s[i])
	rev_word = "".join(comp_list)
	if rev_word.casefold() == new_word.casefold():
		return True
	else:
		return False

def is_palindrome2(s: str) -> bool:
	s = [i for i in s.lower() if i.isalnum()]
	return s == s[::-1]

if __name__ == "__main__":
	s = "A man, a plan, a canal: Panama"
	print(is_palindrome2(s))