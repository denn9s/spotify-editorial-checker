import os
import io
from collections import defaultdict

output_root_dir = 'output'
label_values = defaultdict(int)
label_changes = defaultdict(list)
current_index = 0

def main():
	global current_index
	output_list = os.listdir(output_root_dir)
	output_list.sort()
	for file in output_list:
		load(file)
		current_index += 1

def load(file_name):
	global current_index
	file = io.open(output_root_dir + '/' + file_name, 'r', encoding = 'utf-8')
	for line in file:
		if (current_index == 0):
			if 'TOTAL SONGS' not in line:
				split_str = line.rsplit(':', 1)
				label = split_str[0]
				value = int(split_str[1].strip())
				label_values[label] = value
		else:
			compare(file)
		
def compare(file):
	for line in file:
		if ('TOTAL SONGS' not in line):
			split_str = line.rsplit(':', 1)
			label = split_str[0]
			value = int(split_str[1].strip())
			difference = label_values[label] - value
			label_changes[label].append(difference)

if __name__ == '__main__':
	main()
	print(label_changes)