import sys
import os
from datetime import datetime



if not  os.path.exists('bookslist.txt'):
    with open('bookslist.txt', 'x') as f:
        f.write('*'*50)
command = sys.argv





def add():
    book = input('Enter book name: ')
    writer = input('Enter writer name: ')
    with open('bookslist.txt', 'r+') as f:
        lines = f.readlines()
        last_id = 1
        if lines:
            last_id = int(lines[-5].split(':')[1]) + 1
        ele = f'ID : {last_id}\nBook name : {book}\nWriter name : {writer}\nAdded in : {datetime.today().strftime("%d %B %Y")}'
        f.write(f"{ele}\n{'*' * 50}\n")
    return True

def show():
    id = input('Please enter ID: ' )
    f = open('bookslist.txt', 'r+')
    lines = f.readlines()
    for i in range(0, len(lines), 5):
        search = lines[i].split(':')[1].strip()
        if id == search:
            index = i
            range_list = [index, index + 1, index + 2, index + 3, index + 4]
            for i in range(len(lines)):
                    if i in range_list:
                        print(lines[i])
            break
        
        
        
        
def no_book(func):
    def wrapping(*args):
        lines = args[0]
        if lines:
            func(lines)
        else:
            print('There is no book!')
            sys.exit()
    return wrapping




@no_book
def showall(blist):
    with open('bookslist.txt', 'r+') as f:
        print('There are ',len(f.readlines())//5, 'books!')
        print('*' * 50)
        f.seek(0)
        print(*blist, sep='\n')
        
def remove():
    id = input('Enter ID: ' )
    with open('bookslist.txt', 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in range(0, len(lines), 5):
            remove_ele = lines[line].split(':')[1].strip()
            if id == remove_ele:
                index = line
                range_list = [index, index + 1, index + 2, index + 3, index + 4]
                file.truncate()
                for i in range(len(lines)):
                    if i not in range_list:
                        file.write(lines[i])
                print('\nSuccesfully deleted!\n')
                break
        else:
            print('\nID does not exist!\n')
            
if "add" in command:
    add()
elif "show" and "book" in command:
    show()
elif "all" in command:
    with open('bookslist.txt', 'r+') as file:
        line = file.readlines()
        showall(line)
elif "remove" in command:
    remove()
else:
    print('Wrong input!')