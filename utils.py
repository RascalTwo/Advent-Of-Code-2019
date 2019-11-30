__version__ = '1.1.0'

from datetime import datetime, timedelta
import os
import shutil
import json
import csv
import time

def load_input(dirpath: str, part: str):
	"""Load input from the text, JSON, or CSV file"""
	abspath = next(abspath for abspath in [os.path.join(dirpath, part + ext) for ext in ('.txt', '.json', '.csv')] if os.path.exists(abspath))
	with open(abspath, 'r', newline='') as f:
		if abspath.endswith('.txt'):
			return f.read().strip()
		elif abspath.endswith('.json'):
			return json.load(f)
		elif abspath.endswith('.csv'):
			reader = csv.DictReader(f)
			return [row for row in list(reader)]

def run_solution(solver, data, part: str):
	"""Run the given solver, while timing its execution"""
	start = time.time()
	print(f'Solving {part.upper()}...')
	solver(data)
	print(f'Finished in {round(time.time() - start, 2)} seconds')

if __name__ == '__main__':
	day = (datetime.now() + timedelta(days=1)).day
	day_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), str(day))
	if not os.path.exists(day_path):
		print(f'Generating {day} files')
		os.mkdir(day_path)
		shutil.copy('template.py', os.path.join(day_path, 'solution.py'))
		for part in ['a', 'b']:
			with open(os.path.join(day_path, part + '.txt'), 'w') as f:
				pass
	else:
		print('Nothing to do')
