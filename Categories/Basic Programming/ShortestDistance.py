"""
	Problem completed by Dylan Alexander on 02/04/2022
	This Problem was asked by Google
	You are given an M by N matrix consisting of booleans that represents a board. 
	Each True boolean represents a wall. Each False boolean represents a tile you can walk on.
	Given this matrix, a start coordinate, and an end coordinate, return the minimum 
	number of steps required to reach the end coordinate from the start. If there is no 
	possible path, then return null. You can move up, left, down, and right. You cannot move 
	through walls. You cannot wrap around the edges of the board.
	For example, given the following board:
	[
		[f, f, f, f],
		[t, t, f, t],
		[f, f, f, f],
		[f, f, f, f],
	]
	and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps 
	required to reach the end is 7, since we would need to go through, (1, 2) because there is a 
	wall everywhere else on the second row.
	Solution inspired by https://galaiko.rocks/posts/dcp/maze/
"""

from dataclasses import astuple, dataclass
import numpy as np

def find_path(maze: np.array([list[int], list[int]]), start: list[int], end: list[int]) -> int:
	"""All cells in the given 2D Array are either a 1 - Wall or 0 - Path 

	Args:
		maze (np.array): 2D Array of the Maze
		start (list[int]): Starting position
		end (list[int]): Ending position

	Returns:
		int: Number of steps in the shortest path
	"""
	try:
		maze[start[0]][start[1]] = -1
		mark(maze, start, 0)

	except BaseException as err:
		print(f"Unexpected {err=}, {type(err)=}")
		raise

	return maze[end[0]][end[1]]

@dataclass
class Pos:
	"""	Structure to hold all cell coordinates.
		This object is iterable.
	"""
	i: int
	j: int

	def __iter__(self):
		return iter(astuple(self))

def mark(maze: np.array([list[int], list[int]]), point: list[int], n: int) -> None:
	"""	Marks all the neighbors of a given cell with n + 1

	Args:
		maze (np.array): 2D Array of the Maze
		point (list[int]): Current position
		n (int): Index
	"""
	i, j = point[0], point[1]

	neighbors = {
		tuple(Pos(i + 1, j)): False,
		tuple(Pos(i - 1, j)): False,
		tuple(Pos(i, j + 1)): False,
		tuple(Pos(i, j - 1)): False
	}

	for p in range(0, len(neighbors) - 1):
		neighbors[p] = mark_p(maze, i, j, n+1)

	for p, ok in neighbors.items():
		if (ok):
			mark(maze, np.array([[p.i], [p.j]]))

def mark_p(maze: np.array([list[int], list[int]]), i: int, j: int, n: int) -> bool:
	""" Marks the current position in the maze (maze[i][j]) with given n if 
		it has not been marked.

	Args:
		maze (np.array): 2D Array of the Maze
		i (int): XCoord of Current Position
		j (int): YCoord of Current Position
		n (int): Index

	Returns:
		bool: Returns true if its been marked, false otherwise
	"""
	if i >= len(maze) or j >= len(maze[0]):
		return False
	if i < 0 or j < 0:
		return False
	if maze[i][j] != 0:
		return False

	maze[i][j] = n
	return True

if __name__ == "__main__":
	f, t = 1, 0
	board = [
			[f, f, f, f],
			[t, t, f, t],
			[f, f, f, f],
			[f, f, f, f],
			]
	# Still need to verify if output is correct
	shortest_path = find_path(board, start=[3,0], end=[0,0])
	print(shortest_path)