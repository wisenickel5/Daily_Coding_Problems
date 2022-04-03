'''
Completed by Dylan J. Alexander on 4/3/2022
This problem was asked by Microsoft. (It was an actual interview question
that I was asked to solve but miserably failed at the time).

Print all combinations of numbers from 1 to n having sum n.
For example if n = 5, then the output should be:
[	
	[5], 
	[1, 4], 
	[2, 3], 
	[1, 1, 3], 
	[1, 2, 2], 
	[1, 1, 1, 2], 
	[1, 1, 1, 1, 1]
]

Hint: To avoid permutations, combinations should be constructed in ascending order.
Reference: https://www.techiedelight.com/print-all-combination-numbers-from-1-to-n/
'''

def Sum_Combinations(start: int, num: int, out: list[int], index: int) -> None:
	"""The goal is to consider every integer 'i' from 1 to n, add it to the output, and
	recurse over the remaining elements [i ... n] with reduced sum 'n - i'.
	If a combination with a given sum is reached, we print it.

	Args:
		start (int): _description_
		num (int): _description_
		out (list[int]): _description_
		index (int): _description_

	Time Complexity: O(n)
	"""
	# Print the Combination if the sum becomes 'n'
	if num == 0:
		print(out[:index])
	
	# Start from the previous element in the combination till 'n'
	for j in range(start, num + 1):
		# Place the current element at the current index  
		out[index] = j

		# Recurse with a reduced sum and an increased index
		Sum_Combinations(j, num - j, out, index + 1)

if __name__ == '__main__':
	num = 5
	out = [None] * num
	Sum_Combinations(1, num, out, 0)
