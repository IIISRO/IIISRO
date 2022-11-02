def cubic(r):
    if type(r)==str:
        raise TypeError
    return r**3


def achecker(arr):
    last_arr = []
    for i in arr:
        if 'a' in i:
            last_arr.append(i)
    print(last_arr)        
    return last_arr

def capta(s):
    if type(s)!=str:
        raise TypeError
    return s.capitalize()

class Person:
    def __init__(self, name, surname):  
        self.name = name  
        self.surname = surname 

    def get_fullname(self):
        full_name = f'{self.name.capitalize()} {self.surname.capitalize()}'
        return full_name

class Error(Exception):
    """Base class for other exceptions"""
    pass


class InsufficientAmount(Error):
    """Raised when the input value is too small"""

    pass

class Wallet:

    balance = 0

    def __init__(self, balance):
        self.balance = balance

    def spend_cash(self,x):
        try:
            if self.balance < x:
                raise InsufficientAmount
            self.balance = self.balance - x
            return self.balance
        except InsufficientAmount:
            print('InsufficientAmount')
            return InsufficientAmount


    def add_cash(self,x):
        self.balance = self.balance + x
        return self.balance    