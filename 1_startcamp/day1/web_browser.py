import webbrowser

keywords = [
    'python',
    'javascript',
    'ruby',
    'java'
]

for keyword in keywords:
    url = 'https://www.google.com/search?q=' + keyword
    webbrowser.open_new_tab(url)

