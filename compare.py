import os
import io

output_root_dir = 'output'

def main():
	output_list = os.listdir(output_root_dir)
	output_list.sort()
	for file in output_list:
		load(file)

def load(file_name):
	file = io.open(output_root_dir + '/' + file_name, 'r', encoding = 'utf-8')
	pass

if __name__ == '__main__':
	main()