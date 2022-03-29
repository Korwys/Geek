# Task 1

new_list = [1, 2.34, 'str', None, False, True, [1, 2], {3, 4}, {'name': "Dan"}]

for i in new_list:
    print(f'{i} - {type(i)}')

# Task 2

my_list2 = list(input('Введите числа без пробелов: '))

for i in range(1,len(my_list2),2):
    my_list2[i-1], my_list2[i] = my_list2[i], my_list2[i-1]

print(my_list2)

ret = input('Введите числа без пробелов: ').split()
print(ret)
idx = len(ret) if len(ret) % 2 == 0 else len(ret) - 1

ret[:idx:2], ret[1:idx:2] = ret[1:idx:2], ret[:idx:2]

print('Измененный список', ret)

# Task 3

user_answer = int(input('Введите номер месяца'))

user_year = {1: "Winter", 2: "Winter", 3: "Spring", 4: "Spring", 5: "Spring", 6: "Summer", 7: "Summer", 8: "Summer",
             9: "Auttum", 10: "Autumm", 11: "Autumm", 12: "Winter"}

print(f'Сейчас на дворе {user_year.get(user_answer)}')


# Task 4
user_str = input("Введите значения: ")
a = user_str.split()
for i, z in enumerate(a):
    print(i+1, z)

for i in range(len(a)):
    if len(a[i]) < 10:
        print(f'{i+1} {a[i]}')
    else:
        print(f'{i + 1} {a[i][:10]}')

for i, word in enumerate(a, 1):
    print(f'{i} {word[:10]}')



#Task 5

my_list = [1, 4, 1, 3, 7, 8, 8, 9, 0]
user_answer = int(input('Введите число: '))

if user_answer in my_list:
    f = my_list.index(user_answer)
    a = my_list.count(user_answer)
    my_list.insert(f + a, user_answer)
else:
    my_list.append(user_answer)

print(my_list)
# Task 6
product = [
    (1, {"название": 'model', "цена": 'price', "количество": 'count', "единица": 'value'}),
    (2, {"название": 'model', "цена": 'price', "количество": 'count', "единица": 'value'}),
    (3, {"название": 'model', "цена": 'price', "количество": 'count', "единица": 'value'})
]
tupprod1 = product[0][1]
tupprod2 = product[1][1]
tupprod3 = product[2][1]

for i in tupprod1.keys():
    answer = input(f'Товар 1: Введите {i} : ')
    tupprod1[i] = answer
for i in tupprod2.keys():
    answer = input(f'Товар 2: Введите {i} : ')
    tupprod2[i] = answer
for i in tupprod3.keys():
    answer = input(f'Товар 3: Введите {i} : ')
    tupprod3[i] = answer

print(product)
print('<------------Аналитика---------------->')

values1 = tupprod1.values()
values2 = tupprod2.values()
values3 = tupprod3.values()

analytic = {}

for i in tupprod1.keys():
    analytic[i] = [tupprod1[i], tupprod2[i], tupprod3[i]]


print(analytic)
