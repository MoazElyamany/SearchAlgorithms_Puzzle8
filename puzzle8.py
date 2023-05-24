"""
Puzzle8 Game
-------------
| 0 | 1 | 2 |
-------------
| 3 | 4 | 5 |
-------------
| 6 | 7 | 8 |
-------------
"""

from random import randrange
from SearchAgent import *

def print_puzzle(puzzle):
	p=''
	for i in puzzle:
		if i==0: p+=' '
		else: p+=str(i)
	print (
		'-'*13 + '\n' +
		'| ' + p[0] + ' | ' + p[1] + ' | ' + p[2] + ' |' + '\n' +
		'-'*13 + '\n' +
		'| ' + p[3] + ' | ' + p[4] + ' | ' + p[5] + ' |' + '\n' +
		'-'*13 + '\n' +
		'| ' + p[6] + ' | ' + p[7] + ' | ' + p[8] + ' |' + '\n' +
		'-'*13
		)

def shuffle_puzzle(N):
	#generate a random puzzle by applying N random actions to a sorted puzzle
	puzzle=[0, 1, 2, 3, 4, 5, 6, 7, 8]
	for _ in range(N):
		actions=get_actions(puzzle)
		rand_index=randrange(0,len(actions))
		puzzle=get_state(actions[rand_index],puzzle)
	return puzzle

if __name__ == '__main__':
	puzzle=shuffle_puzzle(50)
	print_puzzle(puzzle)
	for strategy in ['UCS', 'BFS', 'DFS']:
		solution = solve(strategy, puzzle)
		if solution:
			print(f'Using {strategy} strategy:')
			print(f'Solution path: {solution["solution"]}')
			print(f'Number of expanded nodes: {solution["time"]}')
		else:
			print(f'Using {strategy} strategy: No solution found')
			print()
