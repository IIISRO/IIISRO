import requests
import sys

console=sys.argv


if console[1]=='movie':
    moive_name=console[2:]
    response = requests.get(f'http://www.omdbapi.com/?t={moive_name}&apikey=ff79500')
    try:
        response_json=response.json()
        print(f'{"-"*45}\nTitle: {response_json["Title"]}')
        print("Year: ", response_json['Year'])
        print("Released: ", response_json['Released'])
        print("Genre: ", response_json['Genre'])
        print(f'Director: {response_json["Director"]}\n{"-"*45}')
    except:
        print("Movie not found!")
else:
    print("Wrong input!")


