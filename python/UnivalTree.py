# Completed by Dylan Alexander on 1/20/2022
# This problem was asked by Google.
# A unival tree (which stands for "universal value") is a tree where 
# all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
# Solution Found at: https://www.dailycodingproblem.com/blog/unival-trees/

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def CountUnivalSubtree_bf(self, root: list[TreeNode]) -> int:
		# Base Case
		if root is None:
			return 0
		
		left = CountUnivalSubtree_bf(root.left)
		right = CountUnivalSubtree_bf(root.right)

		return 1 + left + right if is_unival(root) else left + right