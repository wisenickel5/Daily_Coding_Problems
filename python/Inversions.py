'''
Problem Solved by Dylan Alexander on 2/26/2022
This problem was asked by Google.
We can determine how "out of order" an array A is by counting the number of inversions it has. 
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element 
appears after a larger element. Given an array, count the number of inversions it has. Do this 
faster than O(N^2) time. You may assume each element in the array is distinct.
For example, a sorted list has zero inversions. 
The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). 
The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
Solution inspired by: https://runzhuoli.me/2018/09/06/count-inversions-in-an-array.html
'''

def brute_force_inversions(arr: list[int]) -> list[tuple([int, int])]:
	sender = []
	for i in range(len(arr) - 1):
		for j in range(len(arr) - 1):
			if arr[i] > arr[j]:
				if i < j:
					sender.append(tuple([arr[j], arr[i]]))
	return sender

def optimal_inversions(arr: list[int]) -> list[tuple([int, int])]:
	return find_inversions(arr, [None]*len(arr), 0, len(arr)-1)

def find_inversions(arr: list[int], temp: list[int], left_start: int, right_end: int) -> list[tuple([int, int])]:
	if left_start >= right_end: # Base Case
		return None

	middle_idx = int((left_start + right_end) / 2)
	left_inversions = find_inversions(arr, temp, left_start, middle_idx)
	right_inversions = find_inversions(arr, temp, middle_idx + 1, right_end)
	split_inversions = find_split_inversions(arr, temp, left_start, right_end)
	return [left_inversions, right_inversions, split_inversions]

def find_split_inversions(arr: list[int], temp: list[int], left_start: int, right_end: int) -> list[tuple([int, int])]:
	sender, count = [], 0
	left_end_idx = int((left_start + right_end) / 2) # Also the middle index
	lp = int(left_start)
	rp = left_end_idx + 1
	right_start = left_end_idx + 1

	for i in range(right_end - left_start):
		if lp > left_end_idx:
			ls_temp = int(left_start + i)
			rp += 1
			temp[ls_temp] = arr[rp]
		
		elif rp > right_end:
			ls_temp = int(left_start + i)
			lp += 1
			temp[ls_temp] = arr[lp]
		
		else:
			if arr[lp] < arr[rp]:
				ls_temp = int(left_start + i)
				lp += 1
				temp[ls_temp] = arr[lp]
			else:
				ls_temp = int(left_start + i)
				rp += 1
				temp[ls_temp] = arr[rp]
				count += int(right_start - lp)
				#sender.append()


if __name__ == "__main__":
	arr = [2, 4, 1, 3, 5]
	
	brute_results = brute_force_inversions(arr)
	print("Brute Force Results: ")
	for i in range(len(brute_results)):
		print(f"{brute_results[i]}", end=" ")

	optimized_results = optimal_inversions(arr)
	print("Optimized Results: ")
	for i in range(len(optimized_results)):
		print(f"{optimized_results[i]}", end=" ")
