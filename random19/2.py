import requests

url=input('Add URL:')

response=requests.get(url)

if response:
    print('Success!')
else:
    print('An error has occurred.')
