import requests
r = requests.get("https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files")
with open('p.htm', 'w', encoding='utf8') as f:
    f.write(r.text)
f.closed
