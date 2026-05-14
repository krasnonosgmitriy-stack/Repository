#my_list = list("hello oleg 2")
#print(my_list)
#my_list = [1, 2, 3]
#my_list[0]=my_list[2]
#print(my_list)
# Створюємо початковий список
#lst = [1, 2, 3]
#print(lst)
# Додаємо елемент у кінець
#list = [1, 2, 3, 4]
#list.append(5)
#print(list)
# Вставляємо елемент за індексом
#list = [1, 2, 3, 4]
#list.insert(2,443)
#print(list)
# Додаємо інший список до початкового
#list = [1, 2, 3, 4]
#list.extend(["oleg"])
#print(list)
from os import remove

# Видаляємо елемент зі значенням 2
#list = [1, 2, 3, 4]
#list.remove(1)
#print(list)

# Видаляємо та виводимо останній елемент
#list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#list.pop(13)
# #print(list)


# Мінімальне та максимальне значення\
#list = [1, 2, 3 ,4 ,5]
#max(list)
#print(max(list))
#print(min(list))


# Довжина списку
#text = "Python"
#print(len(text))


#x = input("прізвище: ")
#y = int(input("бали: "))
#if y > 80:
#    print("здав іспит")
#else:
#    print("не здав")
#x = int(input())
#y = int(input())

#if x > 0 and y > 0:
#    print("first")
#elif x<0 and y > 0:
#    print("second")
#elif x<0 and y<0:
#    print("third")
#else:
#    print("fourth")


#tovar = ("молоко", "хліб", "цукерки", "сир")
#for index, tovar in enumerate(tovar):
#    print(index + 1, tovar)
#shops = ["молоко", "хліб", "цукерки", "сир", "яблоко"]
#for index, shop in enumerate(shops,1):
#    print(index, shop)


#i = int(input())
#del shops[i-1]
#print(shops)



#shops = ["молоко", "хліб", "цукерки", "сир", "яблоко"]
#shops.sort(reverse=True)
#print(shops)

#хрестики нолики
#list = [
#    ["","",""],
#    ["","",""],
#    ["","",""],
#]


###########################################################################
#import random
#
#from colorama import Fore
#
#list2 = int(input("enter field size:"))
#list = [["" for _ in range(list2)] for _ in range(list2)]
#caren_plaer = "x"
#while True:
#    if caren_plaer == "x":
#        for row in list:
#            print(row)
#        print(Fore.RED + "x", end="")
#        column = int(input("Enter a column number")) - 1
#        row = int(input("Enter a row number")) - 1
#    else:
#        list2 = []
#        for i in range(3):
#            for j in range(3):
#                if list[i][j] == "":
#                    list2.append([i, j])
#        column,row = random.choice(list2)
#    if list[row][column] != "":
#        continue
#    list[row][column] = caren_plaer
#    win = False
#    for i in range(3):
#        if list[i][0] == list[i][1] == list[i][2] == caren_plaer:
#            win = True
#        if list[0][i] == list[1][i] == list[2][i] == caren_plaer:
#            win = True
#    if list[0][0] == list[1][1] == list[2][2] == caren_plaer:
#        win = True
#    if list[0][2] == list[1][1] == list[2][0] == caren_plaer:
#        win = True
#    if win:
#        print(f"you win{caren_plaer}")
#        break
#    caren_plaer = "O" if caren_plaer == "x" else "x"


#pogoda = {"kharkiv" : 8, "kiev" : 12, "ternopil" : 15, "lviv" : 20}
#temp = sum(pogoda.values()) / len(pogoda)
#print(temp)

#n = 365
#def sum_to_n(n):
#    if n == 0:
#        return 0
#    return n + sum_to_n(n - 1)
#print(sum_to_n(n))

#shops = ["молоко", "хліб", "цукерки", "сир", "яблоко"]
#shops.sort(reverse=True)
#print(shops)

#shops = ["молоко", "хліб", "цукерки", "сир", "яблуко"]
#
#def oleg(shop):
#    shop.sort(reverse=True)
#    print(shop)
#
#oleg(shops)

#import random

#def create_x(start, stop, count):
#    x = []
#    for i in range(count):
#        number = random.randint(start, stop)
#        x.append(number)
#    x.sort()
#    return x

#def create_y(start, stop, count):
#    y = []
#    for i in range(count):
#        number = random.randint(start, stop)
#        y.append(number)
#    return y

#y = create_y(4,5,6)
#print(y)

#num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#iter1 = iter(num)
#iter2 = filter(lambda x: x % 4 == 0, iter1)
#iter3 = map(lambda x: x % 3, iter2)
#
#for x in iter3:
#    print(x)

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
iter1 = iter(num)
iter2 = filter(lambda i: iter<0,num)
print(iter2)
