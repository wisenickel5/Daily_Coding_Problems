'''
Solved by Dylan Alexander on 4/1/2022
This problem was asked by Microsoft.
A number is considered perfect if its digits sum up to exactly 10.
Given a positive integer n, return the n-th perfect number.
For example, given 1, you should return 19. Given 2, you should return 28.
'''

class PN_Exception(Exception):
	def __init__(self, message: str):
		self.message = message
		super().__init__(message)

def perfect_number(num: int) -> int:
	count = 0
	for i in str(num):
		count += int(i)
		if count > 10:
			raise PN_Exception('Arguement is greater than 10.')
	
	diff = 10 - count
	result = str(num) + str(diff)
	return int(result)


if __name__ == "__main__":
	num = 26
	print(f'Starting Number: {num}... Perfect Number is {perfect_number(num)}!')
