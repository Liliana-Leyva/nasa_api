import requests
import json
import webbrowser
webbrowser.open('http://www.python.org')


K = key


url = 'https://api.nasa.gov/planetary/apod'

#parameters

params = {
    'date' : '2023-08-09',
    'hd' : 'True',
    'api_key': K
}

response = requests.get(url, params=params)
json_data = json.loads(response.text)
image_url = json_data['url']
explanation = json_data['explanation']
title = json_data['title']
print(explanation)
print(title)
webbrowser.open(image_url)
