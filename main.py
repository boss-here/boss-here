import urllib.request
import json


with urllib.request.urlopen('https://www.affirmations.dev/') as response:
    html = json.loads(response.read().decode())

with open('README.md', 'r+') as fp:
    fp.truncate(0)
    fp.write("## " + html['affirmation'])
