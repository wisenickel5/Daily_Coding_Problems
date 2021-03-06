# Completed by Dylan J Alexander on 01/27/2022
# This problem was asked by Twitter.
# You run an e-commerce website and want to record the last N order ids in a log. 
# Implement a data structure to accomplish this, with the following API:
# - record(order_id): adds the order_id to the log
# - get_last(i): gets the ith last element from the log. i is guaranteed to 
# You should be as efficient with time and space as possible.
# Solution found at https://tubean.github.io/2020/04/daily-code-15/

class LogDataStructure:
	def __init__(self, n: int) -> None:
		self.max_size = n
		self.circular_buffer = [1] * n
		self.curr_idx = 0
	
	def record(self, order_id: int) -> None:
		"""Records Order Ids by stacking order ids that are
		recieved as arguements and then increments the current
		index property by 1 until the current index == max_size,
		where curr_idx is reset to 0.

		Args:
			order_id (int)
		"""
		# Use the circular buffer to stack the orderIds
		self.circular_buffer[self.curr_idx] = order_id
		self.curr_idx = (self.curr_idx + 1) % self.max_size
	
	def get_last(self, idx: int) -> int:
		"""Gets the ith last element from the log. 

		Args:
			idx (int): index

		Returns:
			int: ith last element in the Log 
		"""
		
		# The 
		divider = self.curr_idx - idx + self.max_size
		indice = divider % self.max_size
		res = self.circular_buffer[indice]
		return res

if __name__ == "__main__":
	lds = LogDataStructure(4)
	id0 = LogDataStructure.record(lds, 100)
	id1 = LogDataStructure.record(lds, 111)
	id2 = LogDataStructure.record(lds, 222)
	id3 = LogDataStructure.record(lds, 333)
	
	index = 3
	last = LogDataStructure.get_last(lds, index)
	print(f"Index: {str(index)}" + f"\nLast Element: {str(last)}")