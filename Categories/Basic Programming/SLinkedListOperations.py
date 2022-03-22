'''
Ref: https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
Ref: https://realpython.com/linked-lists-python/

A linked list is a sequence of data elements, which are connected together via links. 
Each data element contains a connection to another data element in form of a pointer. 
Python does not have linked lists in its standard library.
'''

class L_L_Exception(Exception):
	def __init__(self, message: str) -> None:
		self.message = message
		super().__init__(message) # Ref: https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods

class Node:
	def __init__(self, data: list[object]) -> None:
		self.data = data
		self.next = None

	def __repr__(self) -> str:
		"""# Ref: https://www.pythontutorial.net/python-oop/python-__repr__/ for how to use __repr__.

		Returns:
			str: data formatted as string.
		"""
		return self.data

class SLinkedList:
	def __init__(self, nodes: list[object] = None) -> None:
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

	def __iter__(self) -> None:
		node = self.head
		while node is not None:
			yield node
			node = node.next

	def add_first(self, node: Node) -> None:
		"""Insert node at the beginning of the LL

		Args:
			node (Node)
		"""
		node.next = self.head
		self.head = node

	def add_last(self, node: Node) -> None:
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

	def add_before(self, target_data: object, new_node: Node) -> None:
		if self.head is None:
			raise L_L_Exception("Linked List is empty.")

		if self.head.data == target_data:
			return self.add_first(new_node)

		prev_node = self.head
		for node in self:
			if node.data == target_data:
				prev_node.next = new_node
				new_node.next = node
				return
			prev_node = node

		raise Exception(f'Node with data: {target_data} was not found')

	def add_after(self, target_data: object, new_node: Node) -> None:
		if self.head is None:
			raise L_L_Exception("Linked List is empty.")
		
		for node in self:
			if node.data == target_data:
				new_node.next = node.next
				node.next = new_node
				return

		raise Exception(f'Node with data: {target_data} was not found')

	def remove_node(self, target_data: Node) -> None:
		if self.head is None:
			raise L_L_Exception("Linked List is empty.")

		if self.head.data == target_data:
			self.head = self.head.next
			return

		prev_node = self.head
		for node in self:
			if node.data == target_data:
				prev_node.next = node.next
				return
			prev_node = node

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

class Two_LinkedList_Operations():
	def __init__(self, linked_list1: SLinkedList, linked_list2: SLinkedList) -> None:
		self.LL1 = linked_list1
		self.LL2 = linked_list2

	def merge_2LL(self) -> Node:
		"""Merge 2 Sorted Linked Lists.
		Reference: https://stackoverflow.com/questions/22507197/merging-two-sorted-linked-lists-into-one-linked-list-in-python

		Args:
			l_l1 (SLinkedList): Linked List 1
			l_l2 (SLinkedList): Linked List 2

		Returns:
			SLinkedList: _description_
		"""
		LL1_head = self.LL1.head
		LL2_head = self.LL2.head
		
		# If either of the linked lists are empty, return the one thats not empty
		if LL1_head is None:
			return self.LL2
		if LL2_head is None:
			return self.LL1
		
		# Create a temp_ptr to avoid additional checks in loop.
		head_ptr = temp_ptr = Node(0)
		while not (LL1_head is None or LL2_head is None):
			if LL1_head.data < LL2_head.data:
				curr_node = LL1_head # Remember current lowest node
				LL1_head = LL1_head.next # Move on
			else:
				curr_node = LL2_head # Remember current lowest node
				LL2_head = LL2_head.next # Move on
			
			# Mutate the node after we have moved on to the next node.
			temp_ptr.next = curr_node
			# Advance temp_ptr
			temp_ptr = temp_ptr.next

		temp_ptr.next = LL1_head or LL2_head

		return head_ptr

	def recurs_merge_2LL(self) -> SLinkedList:
		LL1_head = self.LL1.head
		LL2_head = self.LL2.head
		
		# If either of the linked lists are empty, return the one thats not empty
		if LL1_head is None:
			return self.LL2
		if LL2_head is None:
			return self.LL1

		if (LL1_head.data < LL2_head.data):
			LL1_head.next = self.recurs_merge_2LL(LL1_head.next, LL2_head)
			return self.LL1
		else:
			LL2_head.next = self.recurs_merge_2LL(LL2_head.next, LL1_head)
			return self.LL2

if __name__ == "__main__":
	print("#---- LL with chars ----#\n")
	l_l = SLinkedList(nodes = ['a', 'b', 'c', 'd'])
	l_l.add_first(Node('first'))
	l_l.add_last(Node('last'))
	l_l.add_before('b', Node('before b'))
	l_l.add_after('c', Node('after c'))
	l_l.remove_node('d')
	print(l_l.__repr__() + "\n")

	print("#---- LL with ints ----#\n")
	ll2 = SLinkedList(nodes=[1,3,5,7])
	print(ll2.__repr__())
	ll3 = SLinkedList(nodes=[2,4,6,8])
	print(ll3.__repr__() + "\nMerging Linked Lists...\n")
	ll4_head = Two_LinkedList_Operations(ll2, ll3).merge_2LL()
	print(ll4_head.next)

