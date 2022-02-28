# Completed by Dylan Alexander on 01/24/2022
# This problem was asked by Twitter.
# Implement an autocomplete system. That is, given a query 
# string s and a set of all possible query strings, return 
# all strings in the set that have s as a prefix.
# For example, given the query string de and the set 
# of strings [dog, deer, deal], return [deer, deal].

def AutoComplete(s: str, arr: list[str]) -> list[str]:
	if not(len(s) or len(arr)):
		return []

	for idx, word in enumerate(arr):
		for s_char, word_char in enumerate(zip(s, word)):
			print(s_char, word_char)

	results = []
	for idx, word in enumerate(arr):
		for s_char, word_char in enumerate(zip(s, word)):
			if idx > 0: # We can't autocomplete a word if only the first letters match
				if s_char == word_char:
					results.append(word)
					arr.pop(word)
	return results

if __name__ == "__main__":
	s = "de"
	arr = ["dog", "deer", "deal"]
	result = AutoComplete(s, arr)
	
	print(len(result))
	for i in range(len(result)):
		print(result[i], end=" ")