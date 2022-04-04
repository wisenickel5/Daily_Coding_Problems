'''
Problem solved by Dylan J. Alexander on 4/02/2022
This problem was asked by NCR.
Equilibrium index of an array is an index such that the sum of elements at lower indexes 
is equal to the sum of elements at higher indexes. For example, in an array A:
-	Input: A[] = {-7, 1, 5, 2, -4, 3, 0} 
	Output: 3 
	3 is an equilibrium index, because: 
	A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

- 	Input: A[] = {1, 2, 3} 
	Output: -1

Write a function int equilibrium(int[] arr, int n); that given a sequence arr[] of size n, 
returns an equilibrium index (if any) or -1 if no equilibrium indexes exist. 
'''
def Equilibrium_Index(arr: list[int]) -> int:
	total_sum = sum(arr)
	leftsum = 0
	for i, num in enumerate(arr):
		total_sum -= num
		if leftsum == total_sum:
			return i
		leftsum += num
		
	return -1

if __name__ == '__main__':
	arr = [-7, 1, 5, 2, -4, 3, 0]
	arr2 = [1, 2, 3]
	print(f'The equilibrium index for {arr} is {Equilibrium_Index(arr)}')