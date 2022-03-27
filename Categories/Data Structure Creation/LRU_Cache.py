'''
Problem Completed by Dylan Alexander on 03/04/2022
This problem was asked by Google.
Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a 
cache size n, and contain the following methods:
- set(key, value): 	sets key to value. If there are already n items in the 
					cache and we are adding a new item, then it should also 
					remove the least recently used item.

- get(key):	 gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.

Notes: 
- 	It may be helpful to think about the cache storing pages, where the most recently 
	visited pages are stored in a queue.
	
- 	When we want to referece the queue we can use a hashmap.

- 	Keep in mind that to return the Least Recently Used we can make use of two pointers,
	one the points to the front of the queue, one that points to the back.

'''

class Least_Recently_Used:
	def __init__(self, capacity: int) -> None:
		self.cache_size = capacity
		self.lookup = {}

	def set(self, key: int, value: object) -> None:
		"""Add a new element to the cache, pop the last one off.

		Args:
			key (_type_): _description_
			value (_type_): _description_
		"""
		if len(self.lookup) > self.cache_size:
			self.lookup.popitem(last=True)
		
		self.lookup[key] = value

	def get(self, key) -> int:
		if key not in self.lookup:
			return None
		return self.lookup[key]

	def get_lru(self) -> int:
		return tuple(list(self.lookup.items())[-1])

if __name__ == "__main__":
	lru = Least_Recently_Used(3)
	lru.set(1,"Element One |") # This Element should be removed when (1,4) is added. 
	lru.set(2,"Element Two |")
	lru.set(3,"Element Three |")
	lru.set(1,"Element Four |")
	print("LRU Collection: ")
	for i in lru.lookup:
		print(lru.lookup[i], end=" ")
	#print(f"\nGetting Value At Key: {lru.get(1)}")
	print(f"\nGetting Least Recently Used Item: {lru.get_lru()}")