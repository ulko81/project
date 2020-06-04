import requests
page = requests.get('https://exist.ua')
print('status ---', page.status_code)
