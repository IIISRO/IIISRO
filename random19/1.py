import requests
import sys


console=' '.join(sys.argv[1:])

if console == 'words with a meaning similar to ringing in the ears':
    l="/words?ml=ringing+in+the+ears"
elif console == 'words related to duck that start with the letter b':
    l='/words?ml=duck&sp=b*'
elif console=='words related to spoon that end with the letter a':
    l='/words?ml=spoon&sp=*a'
else:
    print('Data not found!')
    
response=requests.get(f'https://api.datamuse.com/{l}')

print(response.text)

##-------------------------------------------------------------------------##

# import requests

# word=input()
# payload_ml={"ml":f"{word}"}


# response=requests.get(f'https://api.datamuse.com/words', params=payload_ml)

# print(response.text)