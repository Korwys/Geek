from functools import reduce
from sys import argv

# Task 1
# name, work_hours, paid_in_hours, prem = argv
#
#
# def salary(argv):
#     return print(f'Итоговая зарплата - {(int(work_hours) * int(paid_in_hours)) + int(prem)}')
#
# salary(argv)

# Task 2
# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#
# result = [my_list[el] for el in range(1,len(my_list)) if my_list[el] > my_list[el - 1]]
#
# print(result)
#Task 3
# tot = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
# print(tot)

#Task 4

# new_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# 
# result = [new_list[el] for el in range(len(new_list)) if new_list.count(new_list[el]) <= 1]
# print(result)

numbers = [ el for el in range(1,10,2)]

def number(a, b):
    return a*b

result = reduce(number, numbers)
print(result)

numbers = ( el for el in range(1,10,2))
sum = 1
for i in numbers:
    sum *= i
print(sum)

# Task 6

# name, s_1 = argv
#
# def sume(argv):
#     for i in count(int(s_1)):
#         if i > 35:
#             break
#         else:
#             print(i)
#
# sume(argv)

name,s_1, s_2, s_3, s_4 = argv

def sume(argv):
    count = 0
    for i in cycle(argv):
        if count > 35:
            break
        else:
            print(i)
            count+=1

sume(argv)

#Task 7
def fist_gen(number):
    rer = 1
    for i in range(1, number + 1):
        rer *= i
        yield rer

for i in fist_gen(5):
        print(i)