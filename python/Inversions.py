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
Solution inspired by: https://medium.com/@ssbothwell/counting-inversions-with-merge-sort-4d9910dc95f0
'''

def brute_force_inversions(arr: list[int]) -> tuple([ int, list[tuple([int, int])] ]):
	sender, counter = [], 0
	for i in range(len(arr)):
		for j in range(len(arr)):
			if arr[i] > arr[j]:
				if i < j:
					counter += 1
					sender.append(tuple([arr[i], arr[j]]))
	return tuple([counter, sender])

def optimal_inversions(arr: list[int]):
	if len(arr) == 1:
		return tuple([0, arr, []])
	else:
		sorted_arr, counter = [], 0
		middle_idx = int(len(arr) / 2)
		left_side = arr[:middle_idx]
		right_side = arr[middle_idx:]

		left_idx, left_side, inversions = optimal_inversions(left_side)
		right_idx, right_side, inversions = optimal_inversions(right_side)

		i, j = 0, 0
		counter = 0 + left_idx + right_idx

		while i < len(left_side) and j < len(right_side):
			if left_side[i] <= right_side[j]:
				sorted_arr.append(left_side[i])
				i += 1
			else: 
				sorted_arr.append(right_side[j])
				inversions.append(tuple([left_side[i], right_side[j]]))
				j += 1
				counter += len(left_side) - i

		sorted_arr += left_side[i:]
		sorted_arr += right_side[j:]
		return tuple([counter, sorted_arr, inversions])

if __name__ == "__main__":
	arr = [2, 4, 1, 3, 5]
	
	brute_results = brute_force_inversions(arr)
	print("Brute Force Results: " + f"\nInversions Count: {brute_results[0]}")
	for i in range(1, len(brute_results)):
		print(f"{brute_results[i]}", end=" ")

	optimized_results = optimal_inversions(arr)
	print("\n\nOptimized Results: " + f"\nInversions Count: {optimized_results[0]}")
	for i in range(2, len(optimized_results)):
		print(f"{optimized_results[i]}", end=" ")
