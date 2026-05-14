import oLEG as r
import script1 as w
t = {}

def add_t(user, i, currency, amount, cat):
    if user in r.users:
        if i in t:
            print("Перевод існує")
        if r.users (user)["wallet"][currency] < amount:
                print(user, "Недостатньо коштів, поповніть рахунок")
        else:
            t[i] = {"user": user, "currency": currency, "amount": amount, "cat": cat}
            r.users [user]["wallet"][currency] -= amount
            print(user, "Транзакція виконана")
    else:
        print(user, "Авторизуйтесь за допомогою register_user")

def edit_t(i, cat = None):
    if i not in t:
        print("Переводу не існує")
    else:
        if cat:
            t[i]["cat"] = cat

def delete_t(i):
    if i not in t:
        print("Переводу не існує")
    else:
        t.pop(i)
        print("транзакцию видалено")

def my_t(user):
    if user in r.users:
        found = False
        for i, data in t,items():
            if data["user"] == user:
                print(i, data)
                found = True
            else:
                print(user,"витрат немає")
    else:
        print(user,"Авторизуйтесь за допомогою register_user")