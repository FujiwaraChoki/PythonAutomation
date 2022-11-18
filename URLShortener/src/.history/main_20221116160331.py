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
			KEY = 'd829f629708e423310a0b56df800716c3f748'
			url = urllib.parse.quote(sys.argv[1])
			r = requests.get('http://cutt.ly/api/api.php?key={}&short={}&name={}'.format(KEY, url, get_random_string()))
			response = json.loads(r.text)
			show_result(response.get("url")["shortLink"], response.get("url")["title"])
			show_result(short_url, title)

if __name__ == '__main__':
	main()