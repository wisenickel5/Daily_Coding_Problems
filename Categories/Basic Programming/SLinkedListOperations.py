'''
Ref: https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
Ref: https://realpython.com/linked-lists-python/

A linked list is a sequence of data elements, which are connected together via links. 
Each data element contains a connection to another data element in form of a pointer. 
Python does not have linked lists in its standard library.
'''

class Node:
	def __init__(self, data: list[object]):
		self.data = data
		self.next = None

	def __repr__(self) -> str:
		"""# Ref: https://www.pythontutorial.net/python-oop/python-__repr__/ for how to use __repr__.

		Returns:
			str: data formatted as string.
		"""
		return self.data

class SLinkedList:
	def __init__(self, nodes: list[object] = None):
		"""Create a linked list in O(N) time with some data passed as an arguement.

		Args:
			nodes (list[int], optional): Data for our nodes. Defaults to None.
		"""
		self.head = None
		if nodes is not None:
			node = Node(data=nodes.pop(0))
			self.head = node
			for elem in nodes:
				node.next = Node(data=elem)
				node = node.next

	def __iter__(self):
		node = self.head
		while node is not None:
			yield node
			node = node.next

	def add_first(self, node: Node):
		"""Insert node at the beginning of the LL

		Args:
			node (Node)
		"""
		node.next = self.head
		self.head = node

	def add_last(self, node: Node):
		"""Insert node at the end of the LL

		Args:
			node (Node)
		"""
		if self.head is None:
			self.head = node
			return
		for curr_node in self: # Making use of our  __iter__ function.
			pass
		curr_node.next = node

	def add_before(self, target_data: object, new_node: Node):

		return

	def add_after(self, target_data: object, new_node: Node):
		if self.head is None:
			raise Exception("Linked List is empty.")
		
		for node in self:
			if node.data == target_data:
				new_node.next = node.next
				node.next = new_node
				return

		raise Exception(f'Node with data: {target_data} was not found')

	def __repr__(self):
		"""Used to print linked list in the terminal.

		Returns:
			str: List of nodes joined together as a string.
		"""
		node = self.head
		nodes = []
		while node is not None:
			nodes.append(node.data)
			node = node.next
		nodes.append("None")
		return " -> ".join(str(x) for x in nodes)

if __name__ == "__main__":
	l_l = SLinkedList(nodes = ['a', 'b', 'c', 'd'])
	l_l.add_first(Node('first'))
	l_l.add_last(Node('last'))
	l_l.add_before('b', Node('before b'))
	l_l.add_after('c', Node('after c'))
	print(l_l.__repr__())