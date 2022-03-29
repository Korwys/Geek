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

#Task 2
def user_info(**kwargs):
    user = [i for i in kwargs.values()]
    print(" ".join(user))

    user2 = ""
    for i in kwargs.values():
        user2 = f'{user2} {i}'
    print(user2)

user3 = lambda **kwargs: " ".join(kwargs.values())

if __name__ == '__main__':
    # print(user3(name='Oleg', surname='Filipov', date='12.02.1990', city='Moscow', email="sfdsdf@gmail.com")) #Task 2
    # user_info(name='Oleg', surname='Filipov', date='12.02.1990', city='Moscow', email="sfdsdf@gmail.com") #Task 2


