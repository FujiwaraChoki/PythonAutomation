import urllib
import requests
import sys
import random
import json
import PySimpleGUI as sg

def show_result(result_url: str, title: str):
	layout = [
		[sg.Text(f'Shortened URL: {result_url}')],
		[sg.Text(f'Title: {title}')]
	]

	window = sg.Window('', layout=layout, resizable=True, finalized=True)
	window.Maximize()

	# Check for closed window event
	while True:
		event, values = window.read()
		if event == sg.WIN_CLOSED:
			break

def get_random_string():
	LETTERS = 'QWERTZUIOPASDFGHJKLYXCVBNMqwertzuiopasdfghjklyxcvbnm1234567890'
	string = ''
	for i in range(6):
		string += random.choice(LETTERS)
	return string

def main():
	layout = [
		[sg.Text('URL:'), sg.InputText(key='url')],
		[sg.Button('Shorten')]
	]

	window = sg.Window('URL Shortener', layout=layout, resizable=True, finalized=True)
	window.Maximize()

	# Check for closed window event

	while True:
		event, values = window.read()
		if event == sg.WIN_CLOSED:
			break
		if event == 'Shorten':
			url = values['url']
			if not url:
				continue
			if not url.startswith('http'):
				url = 'http://' + url
			try:
				r = requests.get(url)
			except requests.exceptions.ConnectionError:
				continue
			title = r.headers['title']
			short_url = f'https://shorturl.com/{get_random_string()}'
			show_result(short_url, title)

if __name__ == '__main__':
	main()