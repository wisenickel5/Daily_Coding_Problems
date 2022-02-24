'''
Problem completed by Dylan Alexander 2/24/2022
This problem was asked by Amazon.
Implement a stack that has the following methods:
push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
Alternate Solution: https://github.com/ruppysuppy/Daily-Coding-Problem-Solutions/blob/master/Solutions/154.py
'''

class Stack:
	def __init__(self) -> None:
		self.values = []

	def push(self, new_val: int) -> None:
		self.values.insert(0, new_val)

	def pop(self) -> int:
		if len(self.values) == 0:
			raise Exception("(pop) There are no elements within the stack")
		new_stack = []
		pop_val = int
		for idx, val in enumerate(self.values):
			if idx == 0:
				pop_val = self.values[0]
			elif idx >= 1:
				new_stack.append(val)
		self.values = new_stack
		print(f"Popped {pop_val} off the stack")
		print("Current Stack: ")
		for i in range(len(self.values)):
			print(str(self.values[i]), end=" ")
		return pop_val

	def max_value(self) -> int:
		if len(self.values) == 0:
			raise Exception("(max_value) There are no elements within the stack")
		counter = 0
		for i in self.values:
			if i > counter:
				counter = i
		print(f"\nMax value within the stack: {counter}")
		return counter

if __name__ == "__main__":
	test_stack = Stack()
	test_stack.push(100)
	test_stack.push(200)
	test_stack.push(300)
	test_stack.push(400)
	test_stack.push(500)
	biggest = test_stack.max_value()
	popped = test_stack.pop()
	
