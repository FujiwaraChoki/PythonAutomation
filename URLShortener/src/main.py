import urllib
import requests
import pyperclip
import random
import json
import PySimpleGUI as sg

sg.theme('DarkAmber')

def show_result(result_url: str, title: str):
	layout = [
		[sg.Text(f'Shortened URL: {result_url}')],
		[sg.Text(f'Title: {title}')],
		[sg.Button('Copy to clipboard'), sg.Button('Close')]
	]

	window = sg.Window('', layout=layout, resizable=True, finalize=True)

	# Check for closed window event
	while True:
		event, values = window.read()
		if event == sg.WIN_CLOSED:
			break
		if event == 'Copy to clipboard':
			pyperclip.copy(result_url)
			sg.popup('Copied to clipboard')

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

	window = sg.Window('URL Shortener', layout=layout, resizable=True, finalize=True)

	# Check for closed window event
	while True:
		event, values = window.read()
		if event == sg.WIN_CLOSED:
			break
		if event == 'Shorten':
			KEY = 'YOUR_CUTTLY_API_KEY'
			url = urllib.parse.quote(values['url'])
			r = requests.get('http://cutt.ly/api/api.php?key={}&short={}&name={}'.format(KEY, url, get_random_string()))
			response = json.loads(r.text)
			show_result(response.get("url")["shortLink"], response.get("url")["title"])

if __name__ == '__main__':
	main()
