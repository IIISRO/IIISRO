class Number():

    def __init__(self , value):
        self.value = value

    def __add__(self , new):
        return self.value + new.value

    def __mul__(self , new):
        return self.value * new.value
    def __gt__(self , new):
        if(self.value > new.value):
            return True
        else:
            return False

    def __lt__(self , new):
        if(self.value < new.value):
            return True
        else:
            return False

    @classmethod        
    def show_value(cls, value):
        cls.value = value
        return cls.value

number_1=Number(14)
number_2=Number(66)
print(number_1+number_2)
print(number_1*number_2)
print(number_1>number_2)
print(number_1<number_2)
print(Number.show_value(5))

# ++++++++++++++++++++++++++++++++++++++ #
           #  animal task #

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def eating():
        pass
    def moving():
        pass

class Cat(Animal):

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def eating(self):
        print("Cat eating")

    def moving(self):
        print("Cat moving")
