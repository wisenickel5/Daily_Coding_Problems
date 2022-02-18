'''
This problem was solved by Dylan Alexander on 02/18/2022
This problem was asked by Google.
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
You may also use a list or array to represent a set.
'''

def power_set(set: list) -> list:
	"""We first start by creating a 2D Array and then iterating through each element in the set.
	Within each iteration of the set passed as an arguement, we iterate through each subset of 
	the current power set and then create a copy of that subset. With the copy created, we append
	the element of our outer most loop to the copy, and append it to extra_sets which resets with 
	iteration of the given set. After all subsets of the current power_set have been iterated through,
	we append the finalized extra_set to the power_set with the .extend() function.

	Args:
		set (list): Initial Set

	Returns:
		list: Power Set
	"""
	power_set = [[]] # The power set will always contain an empty set

	for element in set:
		extra_sets = []
		for subset in power_set:
			subset_copy = [subset_element for subset_element in subset]
			subset_copy.append(element)
			extra_sets.append(subset_copy)
		# Append each element from extra_sets to powerset
		power_set.extend(extra_sets)

	return power_set

if __name__ == "__main__":
	print(power_set([1,2,3]))