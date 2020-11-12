import os
import io
from collections import defaultdict

output_root_dir = 'output'
label_values = defaultdict(int)
initialized = False

def main():
	output_list = os.listdir(output_root_dir)
	output_list.sort()
	for file in output_list:
		load(file)

def load(file_name):
	global initialized
	file = io.open(output_root_dir + '/' + file_name, 'r', encoding = 'utf-8')
	for line in file:
		if (initialized == False):
			if 'TOTAL SONGS' not in line:
				split_str = line.split(':')
				label = split_str[0]
				value = int(split_str[1].strip())
				label_values[label] = value
				initialized = True
		else:
			compare(file)
		
def compare(file):
	pass

if __name__ == '__main__':
	main()