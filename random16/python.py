import sys
import os
from datetime import datetime, timedelta

from pendulum import date

# #1
# dir=os.getcwd()
# print('My OS:', os.uname().sysname)
# print("Current Directory:", os.getcwd())
# print("Files:", os.listdir(dir))


# #2
# print("Before dir:", os.getcwd())
# os.chdir("..")
# print("After dir:", os.getcwd())


# #3
# dir=os.getcwd()
# os.mkdir(f'{dir}/New Folder')


# #4
# print("a)", datetime.now())
# print("b)", datetime.today().strftime("%Y"))
# print("c)", datetime.today().strftime("%m"))
# print("d)", datetime.today().strftime("%U"))
# print("e)", datetime.today().strftime("%a"))
# print("f)", datetime.today().strftime("%j"))
# print("g)", datetime.today().strftime("%d"))
# print("h)", datetime.today().strftime("%w"))


# #5
# print("Today", datetime.now())
# print("5days later", datetime.now() - timedelta(days=5))


# #6
# for i in range(1,6):
#     print(datetime.now() + timedelta(days=i))


# #7
# date1=input('Input date 1 (yyyy/mm/dd)')
# date2=input('Input date 2 (yyyy/mm/dd)')
# print((datetime.strptime(date1, "%Y/%m/%d"))-(datetime.strptime(date2, "%Y/%m/%d")))



# #8
# birth=input("Write your birthyear:")
# now=datetime.today().strftime("%Y")
# print("Your age:", int(now)-int(birth))
