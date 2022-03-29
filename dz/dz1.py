first_day = int(input('Сколько вы пробежали: '))
final = int(input('Какого результата хотите достичь: '))
new_result = int(input('Ежедневное увеличение в %: '))
daiy_push = 1 + (new_result / 100)
next_daily = first_day
i = 1
while next_daily <= final:
    next_daily = next_daily * daiy_push
    i += 1

print(i)

revenue = int(input('Выручка: '))
cost = int(input('Затраты: '))

if revenue > cost:
    print('У вас все окичи')
    value = revenue - cost
    print(f'Рентабельность равна - {(value/cost):.0%}')
elif revenue == cost:
    print('На тоненького')
else:
    print('Вы в жопе')

people = int(input('Сколько у вас сотрудников: '))
print(f'Прибыль на одного сотрудника равна - {int(value/people)}')


# i = 3481561
# r = -1
# while i > 10:
#     d = i % 10
#     i //= 10
#     if d > r:
#         r = d
# print(r)


# numbers = input('Введите число')
# print(f'Это будет {int(numbers)+int(numbers+numbers)+int(numbers+numbers+numbers)}')


# numbers = input('Введите число')
# new_list = [numbers]
#
# for i in len(new_list):
#     print(i)
