#for i in range(-10, 0):
#   print(i)
import math
from fnmatch import translate

#x = str(input(15))
#rint(x)
#print(type(x))

#s = "p0y1t2h3o4n5_i6s7_c8o9o0l!"
#x = s[:11:2]
#print(x)
#x = s[13:16:2]
#print(x)
#x = s[18::2]
#print(x)

#x = "hEllo wOrld"
#print(x.find("o"))

#x = "hEllo wOrld"
#print(x.count("o"))

#x = "hE.llo wOrld"
#y = x.slit(".")
#print(y)


#x = "  hE.llo wOrld"
#print(x)
#print(x.strip())


#x = "hEllo wOrld"
#print = (x.replace("hello","bye"))

#map = {ord("f"):"ф", ord("u"):"ю"}

#x = "funure"
#translate = x.translate(map)
#print(translate)

#print("pi: {:0.3})".format(3.1415926))



#print("-" * 78)
#print("| {:^3} | {:<20} | {:^10} | {:^10} |".format("№", "Товар", "кількість", "вартість"))
#print("-" * 78)

#print("| {:^3} | {:<20} | {:^10} | {:^10} |".format("1", "Апельсин", "6", "150"))

#print("| {:^3} | {:<20} | {:^10} | {:^10} |".format("2", "Лимон", "8", "90"))

#print("| {:^3} | {:<20} | {:^10} | {:^10} |".format("3", "Картопля", "123", "445"))
#print("-" * 78)
#print("| {:<48} | {:^10} |".format("Продано всього", "685"))
#print("-" * 78)


#def table(surname, people_count):
#    print(f"Бронювання на прізвище: {surname}")
#    print(f"Кількість людей: {people_count}")
#
#    if people_count > 5:
#        print("Кількість людей більша за 5. Пропонуємо другий столик.")
#    else:
#        print("Один столик успішно заброньовано.")
#
#
#surname = input("Введіть прізвище клієнта: ")
#people = int(input("Введіть кількість людей: "))
#
#table(surname, people)


#def OLeG(surname):
#    print(f"пр: {surname}")
#surname = ("oleg")
#OLeG(surname)


#kyb = lambda x: x ** 3
#print(kyb(5))

#krat = lambda x, y: y % x == 0
#print(krat(10, 100))

#sered = lambda x, y: (x + y) % 2
#print(sered(10, 101))

#pifa = lambda x, y: (x ** 2 + y ** 2) ** 0.5
#print(pifa(5, 7))


#currencies = {'USD':  36.9, 'EUR': 38.18, 'GBP': 43.87}
#currencies["pls"] = 9
#currencies["USD"] = 42
#currencies["EUR"] = 47
#currencies["GBP"] = 1
#print(currencies)
#ob = 1000*currencies["USD"]
#print(ob)

#s = "Дано рядок який містить довільне речення"
#
#words = s.split(" ")
#max_word = words[0]
#
#for i in words[1:]:
#    if len(i) > len(max_word):
#        max_word = i[:]
#
#print(max_word)


#d1 = {"USD":100, "EUR":500, "UAH":1000}
#d2 = {"USD":200, "EUR":300, "UAH":2000}
#d3 = {"USD":300, "EUR":500, "UAH":200}
#
#kurs = {"USD-EUR":1.5, "USD-UAH":42, "EUR-UAH":50}
#
#users = {
#    "Oleg": d1,
#    "Oleh": d2,
#    "Olesha": d3
#}
#
#def crefte_wallet(username, USD, EUR, UAH):\
#    users[username] = {"USD":USD, "EUR":EUR, "UAH":UAH}
#
#def show_wallets(username):
#    for user, wallet in users.items():
#        if user == username:
#            print(f"Гаманець{user}: {wallet}")
#            return
#        print("не знайдено")
#
#def change_rate
#
#def convert(val1, val2, amount):
#    res_amount = kurs[f"{val1}-{val2}"]*amount
#    d1[val1] = d1[val1] - amount
#    d1[val2] = res_amount + d1[val2]
#
#print(convert("USD","UAH", 10))
#print(d1)



## Початкові гаманці (не змінюємо)
#d1 = {"USD": 100, "EUR": 500, "UAH": 1000}
#d2 = {"USD": 200, "EUR": 300, "UAH": 2000}
#d3 = {"USD": 300, "EUR": 500, "UAH": 200}
#
## Курси валют
#kurs = {"USD-EUR": 1.5, "USD-UAH": 42, "EUR-UAH": 50}
#
## Користувачі та їх гаманці
#users = {
#    "Ivan": d1,
#    "Anna": d2,
#    "Oleh": d3
#}
#
#
## -------------------------
## 1. Функція створення гаманця
#def create_wallet(username, usd, eur, uah):
#
#    users[username] = {"USD": usd, "EUR": eur, "UAH": uah}
#
#
## -------------------------
## 2. Функція показу гаманця
#def show_wallet(username):
#    for user, wallet in users.items():  # перебираємо всіх користувачів
#        if user == username:             # перевіряємо, чи ім'я співпадає
#            print(f"Гаманець користувача {user}: {wallet}")  # показуємо гаманець
#            return                        # зупиняємо функцію, бо користувача знайшли
#    print("Користувача не знайдено")     # якщо не знайшли, повідомляємо
#
#
## -------------------------
## 3. Функція зміни курсу
#def change_rate(val1, val2, amount):
#
#    kurs[f"{val1}-{val2}"] += amount / 100
#
#
## -------------------------
## 4. Функція конвертації валюти
#def convert(username, val1, val2, amount):
#
#    res_amount = kurs[f"{val1}-{val2}"] * amount  # обчислюємо результат конвертації
#
#    # змінюємо баланс користувача
#    users[username][val1] = users[username][val1] - amount
#    users[username][val2] = users[username][val2] + res_amount
#
#    # змінюємо курс після конвертації
#    change_rate(val1, val2, amount)
#
#
## -------------------------
## Приклади використання
#
## конвертуємо 10 USD в UAH для Івана
#convert("Ivan", "USD", "UAH", 10)
#
## показуємо гаманець Івана
#show_wallet("Ivan")
#
## дивимось, який тепер курс
#print(kurs)
#
## створюємо нового користувача Макса з початковими сумами
#create_wallet("Max", 50, 20, 500)
#
## показуємо його гаманець
#show_wallet("Max")

#vallets=[]
#kurs = {"USD-EUR":1.5, "USD-UAH":42, "EUR-UAH":50, "EUR-USD": 0.66, "UAH-USD":0.024, "UAH-EUR":0.02}
#
#def create_vallet(name,USD,EUR,UAH):
#    return {"name":name,"USD":USD,"EUR":EUR,"UAH":UAH}
#
#def convert(d1,val1, val2, amount):
#    res_amount = kurs[f"{val1}-{val2}"]*amount
#    d1[val1] = d1[val1] - amount
#    d1[val2] = res_amount + d1[val2]
#    change_kurs(val1, val2, amount)
#    print(f"Your wallet is {d1}")
#
#
#def change_kurs(val1, val2, amount):
#    kurs[f"{val1}-{val2}"] += amount/100
#    kurs[f"{val2}-{val1}"] = 1/kurs[f"{val1}-{val2}"]
#
#while True:
#    start = int(input("Welcome to convertor, choose ooperation:\n"
#                    "1 - Start work\n"
#                    "2 - Close\n"))
#    if start == 1:
#        have_vallet = input("Do you have a wallet:\n"
#                            "1 - Yes\n"
#                            "2 - No\n")
#        if have_vallet == "1":
#            convert_opperation = input("Choose convert opperation:\n"
#                                       "1 - USD-UAH\n"
#                                       "2 - USD-EUR\n"
#                                       "3 - UAH-USD\n"
#                                       "4 - UAH-EUR\n"
#                                       "5 - EUR-UAH\n"
#                                       "6 - EUR-USD\n"
#                                       "7 - to start\n")
#            if convert_opperation == "1":
#                name = input("Enter your name:")
#                amount = float(input("Enter your amount:"))
#                for val in vallets:
#                    if val["name"] == name:
#                        convert(val, "USD", "UAH", amount)
#                        continue
#            if convert_opperation == "2":
#                name = input("Enter your name:")
#                amount = float(input("Enter your amount:"))
#                for val in vallets:
#                    if val["name"] == name:
#                        convert(val, "USD", "EUR", amount)
#                        continue
#            if convert_opperation == "3":
#                name = input("Enter your name:")
#                amount = float(input("Enter your amount:"))
#                for val in vallets:
#                    if val["name"] == name:
#                        convert(val, "UAH", "USD", amount)
#                        continue
#            if convert_opperation == "4":
#                name = input("Enter your name:")
#                amount = float(input("Enter your amount:"))
#                for val in vallets:
#                    if val["name"] == name:
#                        convert(val, "UAH", "EUR", amount)
#                        continue
#            if convert_opperation == "5":
#                name = input("Enter your name:")
#                amount = float(input("Enter your amount:"))
#                for val in vallets:
#                    if val["name"] == name:
#                        convert(val, "EUR", "UAH", amount)
#                        continue
#            if convert_opperation == "6":
#                name = input("Enter your name:")
#                amount = float(input("Enter your amount:"))
#                for val in vallets:
#                    if val["name"] == name:
#                        convert(val, "EUR", "USD", amount)
#                        continue
#            if convert_opperation == "7":
#                continue
#
#
#
#        elif have_vallet == "2":
#            create = input("Your name:")
#            valut = float(input("USD:"))
#            valut2 = float(input("EUR:"))
#            valut3 = float(input("UAH:"))
#            vallet = create_vallet(create,valut,valut2,valut)
#            vallets.append(vallet)
#            print(f"Your wallet is {vallet}")
#            continue
#    if start == 2:
#        print("Have a good day!")
#        break

#tri = 3
#prime_num = {2,3,5,7,11,13,17,19,23}
#if 3 in prime_num:
#    print(3 in prime_num)

#user = {
#    "name": "Bill",
#    "surname": "Bosh",
#    "age": 22
#}
#for key,value in user.items():
#    print("da")

#cities = {
#    'Київ'    : 0,
#    'Вінниця' : 240,
#    'Харків'  : 470,
#    'Ужгород' : 808,
#    'Львів'   : 540,
#    'Житомир' : 120,
#    'Одеса'   : 430
#}
#
#bid = max(cities key=cities.get())
#print(f"Bidalene  {bid}")


#surename = {
#    'Івко' : 4,
#    'Маляренко'  : 11,
#    'Стеценко' : 5,
#    'Судакова'   : 12
#}
#for number in surename.values():
#    if number > 10:
#        print(number)
#
#library = {
#    "fantasy": [
#        {"title": "Book1", "author": "Author1", "pages": 450},
#    ],
#    "sci-fi": [
#        {"title": "Book2", "author": "Author2", "pages": 320},
#        {"title": "Book3", "author": "Author3", "pages": 320},
#    ]
#}
#
#def show(slovnik, genre):
#    if genre not in slovnik:
#        print("no such genre")
#    else:
#        for key in slovnik.keys():
#            if key ** genre:
#                print(slovnik[key])
#
#
#show(library, "dasda")
#
#def add(slovnik, genre, title, author, pages):
#    if genre not in slovnik:
#        slovnik[genre] = []
#    book = {"title": title, "author": author, "pages": pages}
#    slovnik[genre].append(book)
#    print(slovnik)
#add(library, "sci-gyjh", "Fantasy", "Author1", 450)

#s = [1,2,-4,566,6,7]
#a = all(x>0 for x in s)
#if a:
#    z = sorted(s)
#    print(z)
#else:
#    print("-")
#import datetime as dt
#from datetime import datetime
#index = int(input(":"))
#dates = [
#    dt.date(2027, 3, 1),
#    dt.date(2027, 3, 2),
#    dt.date(2027, 3#, 3)
#today = dt.date.today()
#dalta = dates[index] - today
#print(dalta)

#cities = {
#    "Київ"    : 0,
#    "Вінниця" : 240,
#    "Харків"  : 470,
#    "Ужгород" : 808,
#    "Львів"   : 540,
#    "Житомир" : 120,
#    "Одеса"   : 430
#}
#
#try:
#    bid = max(cities, key=cities.get)
#    print(f"Найвідалене місто {bid} відстань {cities[bid]} км")
#except ValueError:
#    print("Словник порожній немає міст для пошуку.")


import hashlib
users = {}
def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password
def register_user(username, password):
    if username in users:
        print("Цей логін уже використовується. Оберіть інший.")
    else:
        users[username] = hash_password(password)
        print(f"Користувача {username} успішно зареєстровано.")

def authenticate_user(username, password):
    if username in users:
        hashed_password = hash_password(password)
        if users[username]["pasword"] == hashed_password:
            print(f"Ласкаво просимо, {username}!")
        else:
            print("Невірний пароль. Спробуйте ще раз.")
    else:
        print("Користувача з таким логіном не існує.")

register_user("admin", "admin")
authenticate_user("admin", "admin")
print(users)

#info = {}


#def add(id, amount, kategori):
#    if id in info:
#        print("+")
#    else:
#        info[id] = {"amount": amount, "kategori": kategori}

#add(4,100,"product")
#add(3,1000,"одяг")
#print(info[4])

#def edit_t(id, amount = None, kategori = None):
#    if id not in info:
#        print("перводу не існує")
#    else:
#        if amount:
#            id["amount"] = amount
#            if kategori:
#                id[kategori] = kategori
#    print(info)

#edit_t(2, kategori = "home")

#def delete_t(id):
#    if id not in info:
#        print("переводу не існує")
#    else:
#        t.pop