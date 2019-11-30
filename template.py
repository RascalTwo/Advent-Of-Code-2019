__version__ = '1.0.0'

import sys
sys.path.append('..')
sys.path.append('.')
import os
from utils import load_input


def solve_a(data):
	pass

def solve_b(data):
	pass


if __name__ == '__main__':
	dirname = os.path.dirname(os.path.abspath(__file__))

	for solve, part in ((solve_a, 'a'), (solve_b, 'b')):
		data = load_input(dirname, part)
		print(f'Solving {part.upper()}...')
		solve(data)
		print(f'Finished {part.upper()}')
