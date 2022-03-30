# Task 1

def first_func():
    while True:
        try:
            first = int(input('Введите первое число: '))
            second = int(input('Введите второе число: '))
            result = first / second
        except ZeroDivisionError:
            print('Деление на ноль невозможно')
        except ValueError:
            print('Введите число а не букву')
        else:
            print(result)
            break


# Task 2
def user_info(**kwargs):
    user = [i for i in kwargs.values()]
    print(" ".join(user))

    user2 = ""
    for i in kwargs.values():
        user2 = f'{user2} {i}'
    print(user2)


user3 = lambda **kwargs: " ".join(kwargs.values())


# Task 3

def my_func(*args):
    numbers = list(args)
    mx1 = max(numbers)
    numbers.remove(mx1)
    mx2 = max(numbers)
    print(mx2 + mx1)

    numbers2 = list(args)
    numbers2.sort()
    print(numbers2[-1]+numbers2[-2])


# Task 4
def my_func(x, y):
    y = abs(y)
    print(x ** y)
#Способ через цикл
    i = 0
    result = 1
    while i < y:
        result = result * x
        i += 1
    print(result)


if __name__ == '__main__':
    # print(user3(name='Oleg', surname='Filipov', date='12.02.1990', city='Moscow', email="sfdsdf@gmail.com")) #Task 2
    # user_info(name='Oleg', surname='Filipov', date='12.02.1990', city='Moscow', email="sfdsdf@gmail.com") #Task 2
    # my_func(9,5,10) #Task 3
    # my_func(2, -3) #Task 4
