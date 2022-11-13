import os
import PyPDF2
from termcolor import colored

def main():
	if len(sys.argv) > 1:
		file_name = sys.argv[1]
		pdf_contents_bytes = None
		with open(file_name, 'rb') as cur_file:
			pdf_contents_bytes = cur_file.read()
		pdf_reader = PyPDF2.PdfFileReader(pdf_contents_bytes)

		pdf_content_str = ''
		num_pages = pdf_reader.numPages

		for i in range(num_pages):
			pdf_content_str += pdf_reader.getPage(i).extractText()

		print(colored('Successfully extracted text.', 'green'))
		print(f'Text:\n{pdf_content_str}')

		
	else:
		print(colored('Please provide a PDF file name.', 'red'))		

if __name__ == '__main__':
	try:
		main()
	except Exception as err:
		print(colored('An error has occurred:\n{err}', 'red'))
