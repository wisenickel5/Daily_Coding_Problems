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
'''

def brute_force_inversions(arr: list[int]) -> tuple([int, int]):
	sender = []
	for i in range(len(arr) - 1):
		for j in range(len(arr) - 1):
			if arr[i] > arr[j]:
				if i < j:
					sender.append(tuple([arr[j], arr[i]]))
	return sender

if __name__ == "__main__":
	arr = [2, 4, 1, 3, 5]
	brute_results = brute_force_inversions(arr)
	print("Brute Force Results: ")
	for i in range(len(brute_results)):
		print(f"{brute_results[i]}", end=" ")