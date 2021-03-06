'''
This problem was asked by Microsoft.
Given an array of numbers, find the length of the longest increasing subsequence in the array.
The subsequence does not necessarily have to be contiguous.
For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 
the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
As a bonus, try to return the longest increasing subsequence.
Reference: https://www.dailycodingproblem.com/blog/longest-increasing-subsequence/
'''

def longest_increasing_subsequence(arr: list[int]) -> list[int]:
	"""
	
	Time complexity: O(n^2) 
	"""
	if not arr:
		return 0

	cache = [1] * len(arr) # Contains length of LIS ending at i

	for i in range(1, len(arr)):
		for j in range(i):
			if arr[j] < arr[i]:
				cache[i] = max(cache[i], cache[j] + 1)

	return cache

if __name__ == "__main__":
	arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
	print("\nArguement Array:\n", arr)

	result = longest_increasing_subsequence(arr)
	print("Length of longest increasing subsequence", max(result))