from datetime import datetime
import os

if not os.path.exists('log.txt'):
    with open ("log.txt",'w') as a:
        a.write('|   Function name    |          worked time           |     arguments as list     |  arguments as dictionary  | function result  |\n')


def logger(f):
    # Write task solution here
    def wrapper(*args,**kwargs):
        try:
            cavab=f(*args,**kwargs)
            with open ("log.txt",'a') as a:
                a.write(f'|{"{:<20}".format(f.__name__)}|  ')
                a.write(f'{"{:<30}".format(str(datetime.today()))}|  ')
                a.write(f'{"{:<25}".format(str(args))}|  ')
                a.write(f'{"{:<25}".format(str(kwargs))}|  ')
                a.write(f'{"{:<16}".format(str(cavab))}|  ')
                a.write('\n')
        except  Exception as e:
            with open ("log.txt",'a') as a:
                a.write(f'|{"{:<20}".format(f.__name__)}|  ')
                a.write(f'{"{:<30}".format(str(datetime.today()))}|  ')
                a.write(f'{"{:<25}".format(str(args))}|  ')
                a.write(f'{"{:<25}".format(str(kwargs))}|  ')
                a.write(f'{"{:<16}".format(str(e))}|  ')
                a.write('\n')

    return wrapper    


@logger
def sum(a,b):
    return a+b

@logger
def divide(a,b):
    return a/b




sum(1,2)

divide(a=4,b=2)

divide(10,0)