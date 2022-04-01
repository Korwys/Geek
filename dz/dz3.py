# # Task 1
#
# def first_func():
#     while True:
#         try:
#             first = int(input('Введите первое число: '))
#             second = int(input('Введите второе число: '))
#             result = first / second
#         except ZeroDivisionError:
#             print('Деление на ноль невозможно')
#         except ValueError:
#             print('Введите число а не букву')
#         else:
#             print(result)
#             break
#
#
# # Task 2
# def user_info(**kwargs):
#     user = [i for i in kwargs.values()]
#     print(" ".join(user))
#
#     user2 = ""
#     for i in kwargs.values():
#         user2 = f'{user2} {i}'
#     print(user2)
#
#
# user3 = lambda **kwargs: " ".join(kwargs.values())
#
#
# # Task 3
#
# def my_func(*args):
#     numbers = list(args)
#     mx1 = max(numbers)
#     numbers.remove(mx1)
#     mx2 = max(numbers)
#     print(mx2 + mx1)
#
#     numbers2 = list(args)
#     numbers2.sort()
#     print(numbers2[-1] + numbers2[-2])
#
#
# # Task 4
# def my_func(x, y):
#     y = abs(y)
#     print(x ** y)
#     # Способ через цикл
#     i = 0
#     result = 1
#     while i < y:
#         result = result * x
#         i += 1
#     print(result)
#
#
# # Task 5
#
# def chick():
#     all_s = 0
#     while True:
#         st1 = input("Введите числа: ").split()
#         for i in st1:
#             if i == "q":
#                 print(" Vsego")
#                 return all_s
#             else:
#                 all_s += int(i)
#         print(all_s)
#
#
#
# summary = 0
# try:
#     while summary != '#':
#         for i in map(int, input('tut:').split()):
#             summary += i
#             print(summary)
#  except ValueError:
#     print(summary)
#
#
#
#     all_s = 0
#     while True:
#         try:
#             st1 = list(map(int, input('dea: ').split()))
#         except ValueError:
#             print(f'Вы покинули программу. Итоговая сумма - {all_s}')
#             break
#
#         if "q" in st1:
#             print(all_s)
#             break
#         else:
#             all_s += sum(st1)
#             print(f'Сумма чисел равна - {all_s}')


#Task 6

def int_func():
    user_answer = input("Введите слово: ").title()
    print(user_answer)

if __name__ == '__main__':
    # print(user3(name='Oleg', surname='Filipov', date='12.02.1990', city='Moscow', email="sfdsdf@gmail.com")) #Task 2
    # user_info(name='Oleg', surname='Filipov', date='12.02.1990', city='Moscow', email="sfdsdf@gmail.com") #Task 2
    # my_func(9,5,10) #Task 3
    # my_func(2, -3) #Task 4
    #  chick()
    int_func()


