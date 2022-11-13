import os
import pyperclip
import sys
from termcolor

def main():
	if len(sys.argv) > 0:
		file_name = sys.argv[1]
		contents = ''
		with open(file_name, 'r'):
			contents = file_name.read()
		# Finally copy to clipboard
		pyperclip.copy(contents)

	else:
		print(colored('Please provide a file name!', 'red'))

if __name__ == '__main__':
	try:
		main()
	except Exception as err:
		print(colored(f'An error has occurred:\n{err}', 'red'))