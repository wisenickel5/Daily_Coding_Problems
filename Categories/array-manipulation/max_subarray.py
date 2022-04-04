'''
Problem Completed by Dylan Alexander 03/01/2022
This problem was asked by Amazon.
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, 
since we would take elements 42, 14, -5, and 86. Given the array [-5, -1, -8, -9], 
the maximum sum would be 0, since we would not take any elements.
Do this in O(N) time.
'''

def max_subarray(arr: list[int]) -> int:
	max_so_far = arr[0]
	curr_max = 0

	for i in range(0, len(arr)):
		curr_max = max(arr[i], curr_max + arr[i])
		max_so_far = max(max_so_far, curr_max)
	
	return max_so_far

def max_subarray2(arr: list[int]):
	max_so_far = arr[0]
	curr_max = 0
	 
	for i in range(0, len(arr)):
		curr_max = curr_max + arr[i]
		if curr_max < 0:
			curr_max = 0
		elif (max_so_far < curr_max):
			max_so_far = curr_max
			 
	return max_so_far

if __name__ == "__main__":
	arr = [34, -50, 42, 14, -5, 86]
	arr2 = [-5, -1, -8, -9]
	max_sum = max_subarray(arr2)
	print(f"Max sum is {max_sum}")