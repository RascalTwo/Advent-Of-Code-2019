__version__ = '1.0.0'

# Boilerplate Imports
import sys
sys.path.append('..')
sys.path.append('.')
import os
from utils import load_input, run_solution

# Solution imports
import math


def calcfuel(m):
	m /= 3
	m = math.floor(m)
	m -= 2
	return m

def calcrecur(m):
	yield m
	while True:
		m = calcfuel(m)
		if m <= 0:
			break
		yield m

parse_masses = lambda data: [int(m) for m in data.split('\n')]

def solve_a(data):
	results = []
	masses = parse_masses(data)
	for m in masses:
		results.append(calcfuel(m))

	print(sum(results))

def solve_b(data):
	results = []
	masses = parse_masses(data)
	for m in masses:
		results += list(calcrecur(calcfuel(m)))

	print(sum(results))



if __name__ == '__main__':
	dirname = os.path.dirname(os.path.abspath(__file__))

	for solve, part in ((solve_a, 'a'), (solve_b, 'a')):
		run_solution(solve, load_input(dirname, part), part)
