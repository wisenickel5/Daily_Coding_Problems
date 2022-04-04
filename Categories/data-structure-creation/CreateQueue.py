'''
Completed by Dylan Alexander on 03/10/2022
This problem was asked by Apple.
Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) 
data structure with the following methods: enqueue, which inserts an element into the 
queue, and dequeue, which removes it.
'''

class New_Queue():
	def __init__(self) -> None:
		self.s1 = []
		self.s2 = []

	def brute_enqueue(self, element: int) -> None:
		"""Function ensures that the first element entered is always at the top
		of stack 1. O(n) Time Complexity.

		Args:
			element (int)
		"""
		while (len(self.s1) >= 1):
			self.s2.append(self.s1[-1])
			self.s1.pop()
		
		self.s1.append(element)

		while (len(self.s2) >= 1):
			self.s1.append(self.s2[-1])
			self.s2.pop()

	def simple_enqueue(self, element: int) -> None:
		"""This function pairs with the recursive Dequeue method.

		Args:
			element (int)
		"""
		self.s1.insert(0, element)

	def dequeue(self) -> int:
		"""Returning the last element from stack 1 after its being popped.
		O(1) Time Complexity

		Raises:
			Exception: If stack1 is empty

		Returns:
			int: First item pushed onto queue
		"""
		if len(self.s1) <= 0:
			raise Exception("Queue is empty")
		return self.s1.pop()

	def recurs_dequeue(self) -> int:
		if len(self.s1) <= 0:
			print("Queue is empty")
			return
		
		# Pop item from stack
		x = self.s1[len(self.s1) - 1]
		self.s1.pop()

		# If stack is empty, return popped item
		if len(self.s1) <= 0:
			return x
		
		item = self.recurs_dequeue()
		return item

	def print_queue(self) -> None:
		print("Current Queue: ")
		for i in range(len(self.s1)):
			print(self.s1[i], end=" ")

if __name__ == "__main__":
	que = New_Queue()

	# Brute Force Queue
	que.brute_enqueue(1)
	que.brute_enqueue(2)
	que.brute_enqueue(3)
	print(f"Dequeued element: {que.dequeue()}")
	que.print_queue()

	# Recursive Queue 
	que.simple_enqueue(4)
	que.simple_enqueue(5)
	que.simple_enqueue(6)
	print(f"\nRecursively dequeued element: {que.recurs_dequeue()}")
	que.print_queue()
