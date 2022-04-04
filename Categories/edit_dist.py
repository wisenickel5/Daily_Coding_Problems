'''
Problem completed by Dylan Alexander on 2/25/2022
This problem was asked by Google.
The edit distance between two strings refers to the minimum number of 
character insertions, deletions, and substitutions required to change 
one string to the other. For example, the edit distance between “kitten” 
and “sitting” is three: substitute the “k” for “s”, substitute the “e” 
for “i”, and append a “g”.
Given two strings, compute the edit distance between them
'''

def edit_distance(s1: str, s2: str) -> int:
	counter = 0
	for idx, char in enumerate(s1):
		if idx >= 0:
			if char != s2[idx]:
				counter += 1
		if idx == len(s1) - 1:
			if char != s2[idx]:
				counter += 1

	if len(s1) < len(s2):
		counter += len(s2)-len(s1)
	elif len(s1) > len(s2):
		counter += len(s1)-len(s2)
		
	return counter

if __name__ == "__main__":
	s1, s2 = "kitten", "sitting"
	print(f"Edit distance from {s1} to {s2} is {edit_distance(s1, s2)}")