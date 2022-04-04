# #Task 1-2
# with open('dz5.txt', 'r', encoding='utf-8') as f:
#     # words = input('Введите текст: ')
#     # f.writelines(f'{words}\n')
#     count_str = 0
#     count_words = 0
#     count_letters = 0
#     for i in f:
#         count_str += 1
#         for l in i.split():
#             count_words += 1
#             for o in l:
#                 count_letters += 1
#     print(count_str)
#     print(count_words)
#     print(count_letters)
#
# #Task 3
# with open('dz\workers.txt', 'r',encoding='utf-8') as f:
#     for string in f:
#         vop = string.split()
#         wo = {vop[0]:float(vop[1])}
#         for name,sullary in wo.items():
#             if sullary < 20000:
#                 print(f'{name} - {sullary}')
#
#
# #Task 4
# with open('dz\dz5_Etot.txt', 'w', encoding='utf8') as f:
#     with open('dz\dz5_en.txt', 'r', encoding='utf8') as g:
#         for lines in g:
#             if "One" in lines:
#                 xo = lines.replace("One", "Один")
#                 f.write(xo)
#             if "Two" in lines:
#                 xo = lines.replace("Two", "Два")
#                 f.write(xo)
#             if "Three" in lines:
#                 xo = lines.replace("Three", "Три")
#                 f.write(xo)
#             if "Four" in lines:
#                 xo = lines.replace("Four", "Четыре")
#                 f.write(xo)
#
#         #Способ 2
#         eng = {'One': "Один", 'Two': "Два", 'Three': "Три", 'Four': "Четыре"}
#         f.writelines([i.replace(i.split()[0], eng.get(i.split()[0])) for i in g])
#         #Способ 3
#         text =f1.read()
#           try:
#               f.write(Translator().translate(text,dest='ru').text)
#           except AttributeError:
#               print('Ddos ataka ne ydalas')
#
# #Task 5
# with open('dz5_next.txt', 'r+', encoding='utf8') as f:
#     numbers = [i for i in range(1, 15)]
#     print(numbers)
#     num = ''
#     i = 0
#     while i < 5:
#         num += f' {str(randint(1, 100))}'
#         i += 1
#     f.write(num)
#
#     # Способ 1
#     sumer = [i.split() for i in f]
#     op1 = sum([int(p) for o in sumer for p in o])
#     print(op1)
#     # Способ 2
#     op = 0
#     for k in sumer:
#         for i in k:
#             op += int(i)
#     print(op)
#
# #Task 6
#
# #Способ 1
#     with open('dz\dz5_task6.txt', 'r', encoding='utf-8') as f:
#         # print(f.read())
#         dit = {}
#         for i in f:
#            v = i.replace('-' ,'').replace('(л)' ,'').replace('(пр)' ,'').replace('(лаб)' ,'')
#            name, counts =v.split(":")
#            print(name)
#            new_c = sum(int(i) for i in counts.split())
#            dit[name] = new_c
#         print(dit)

#Task 7
import json

if __name__ == '__main__':

    with open('dz5_taksk7.txt', "r", encoding='utf-8') as f:
        profit = {}
        average_profit = {}
        result = [profit, average_profit]
        for lines in f:
            profit[lines.split()[0]] = int(lines.split()[2]) - int(lines.split()[3])
        average_profit["average_profit"] = sum(i for i in profit.values() if i > 0) / len(profit)
    with open('dz5_task7.json', 'w', encoding='utf-8') as i:
        json.dump(profit, i, ensure_ascii=False,indent=4)
