'''
Completed by Dylan Alexander on 01/12/2022
Given a list of numbers and a number k, 
return whether any two numbers from the 
list add up to k.
'''

def BruteForceTwoSum(arr, k):
    targetLen = len(arr)
    for i in range(0, targetLen):
        for j in range(i + 1, targetLen):
            if (arr[i] + arr[j] == k):
                print("Brute Force" + f"\n[{arr[i]}, {arr[j]}]" + f"\nk = {k}")
                return [i, j]

def OptimizedTwoSum(arr, k):
    seen = {}
    for i, value in enumerate(arr):
        remaining = k - arr[i]
        
        if remaining in seen:
            print("Optimized" + f"\n[{arr[i]}, {seen[remaining]}]" + f"\nk = {k}")
            return [i, seen[remaining]]
        
        seen[value] = i

if __name__ == "__main__":
    test_arr = [10, 15, 3, 7]
    k = 17
    BruteForceTwoSum(test_arr, k)
    OptimizedTwoSum(test_arr, k)