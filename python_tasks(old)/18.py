import sys
import os
from datetime import datetime




if not  os.path.exists('bookslist.txt'):
    with open('bookslist.txt', 'x') as f:
        f.write('*'*50)

command = sys.argv



class Book:
    def set_id(self):
        with open('bookslist.txt', 'r+') as f:
            lines = f.readlines()
            last_id = 1
            if lines:
                last_id = int(lines[-5].split(':')[1]) + 1
            ele = f'ID : {last_id}'
            f.write(f"{ele}\n")
        return True


    def add_book(self):
        book = input('Enter book name: \n')
        author = input('Enter writer name: \n')
        with open('bookslist.txt', 'a+') as f:
                ele = f'Book name : {book}\nWriter name : {author}'
                f.write(f"{ele}\n")
                print('\nAdded successfully!')
    
    
    def set_date(self):
        with open('bookslist.txt', 'a+') as f:
                ele = f'Added in: {datetime.today().strftime("%d %B %Y")}'
                f.write(f"{ele}\n{'*' * 50}\n")
   
   
    def show_all(self):
        with open('bookslist.txt', 'r+') as f:
            lines = f.readlines()
            if len(lines)==0:
                print('There is no book!')
            else:
                print('There are',len(lines)//5, 'books!')
                print('*' * 50)
                f.seek(0)
                for index, line in enumerate(f):
                    if index>=0:
                        print(line)
   
   
    def  show_book(self):
        id = input("Enter ID: \n")
        print('*'*50)
        with open('bookslist.txt', 'r+') as f:
            lines = f.readlines()
        for i in range(0, len(lines), 5):
            search = lines[i].split(':')[1].strip()
            if id == search:
                index = search
                index = i
                with open('bookslist.txt', 'r+') as f:
                    for index_of_line, line in enumerate(f):
                        if index_of_line in range(index,index+5):
                            print(line)
    
    
    def remove_book(self):
        remove_id = input('Enter ID: \n')
        with open('bookslist.txt', 'r+') as f:
            lines = f.readlines()
            f.seek(0)
            for i in range(0, len(lines), 5):
                index = lines[i].split(':')[1].strip()
                if remove_id == index:
                    index_each_line = i
                    f.truncate()
                    for i in range(len(lines)):
                        if i not in range(index_each_line,index_each_line+5):
                            f.write(lines[i])
                    print('\nSuccesfully deleted!\n')
                    break
            else:
                print('\nID does not exist!\n')


library = Book()
if "add" in command:
    library.set_id()
    library.add_book()
    library.set_date()
elif "show" and "book" in command:
    library.show_all()
elif "all" in command:
    library. show_book()
elif "remove" in command:
    library.remove_book()
else:
    print('Wrong input')