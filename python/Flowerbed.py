# Given an integer array flowerbed containing 0's and 1's,
# where 0 means empty and 1 means not empty, and an integer n, 
# return if n new flowers can be planted in the flowerbed 
# without violating the no-adjacent-flowers rule.

def CanPlaceFlowers(flowerbed: list[int], n: int) -> bool:
	zeros, ans = 1, 0  # Easier handling of prefixes, just initialize zeros to 1
	for f in flowerbed:
		if f == 0: 
			zeros += 1
		else:
			ans += (zeros - 1) // 2
			zeros = 0
	return ans + zeros // 2 >= n

if __name__ == '__main__':
	flowerbed = [1,0,0,0,1]
	to_plant = 2
	CanPlaceFlowers(flowerbed, to_plant)