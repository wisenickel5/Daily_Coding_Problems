'''
Given an array of integers, return a new array such that 
each element at index i of the new array is the product 
of all the numbers in the original array except the one at i.
Ex. [1, 2, 3, 4, 5] --> [120, 60, 40, 30, 24]
'''

def Product_Array(arr):
    n = len(arr)
    # Base Case
    if (n == 1):
        return arr

    left = [0] * n
    right = [0] * n
    prod = [0] * n

    left[0] = 1
    right[n - 1] = 1

    # Iterate forwards through the left array 
    for i in range(1, n):
        left[i] = arr[i - 1] * left[i - 1]

    # Iterate backwards through the right array
    for j in range(n - 2, -1, -1):
        right[j] = arr[j + 1] * right[j + 1]

    # Iterate through left & right arrays & 
    # multiply elements
    for i in range(n):
        prod[i] = left[i] * right[i]

    # Print the arrays
    print("Left Array:\n", left)
    print("\n\nRight Array:\n", right)
    print("\n\nResult Array:\n", prod)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    Product_Array(arr)