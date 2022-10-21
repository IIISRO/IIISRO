import sys
import datetime


t=datetime.datetime.now()
if '-' in sys.argv:
    tre=sys.argv.index('-')
    if '-' in sys.argv and len((sys.argv)[(tre+1):])!=0  and len((sys.argv)[1:tre])!=0:
        print("Book name: ", *(sys.argv)[1:tre])
        print("Writer: ", *(sys.argv)[(tre+1):])
        print("Added in: ", t.strftime("%d %B %Y"))
    else:
        print("Wrong input")
else:
    print("Wrong input")

































