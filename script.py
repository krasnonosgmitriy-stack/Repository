import oLEG as r
def wallet(user, USD, EUR, UAH):
    if user in r.users:
        r.users[user]["wallet"] = {
            "USD": USD,
            "EUR": EUR,
            "UAH": UAH }
    else:
        print(user, "авторизуйся за допомогою register_user")

cost = {"USD-UAH":44,
        "USD-EUR":0.9,
        "UAH-USD":0.023,
        "UAH-EUR":0.020,
        "EUR-USD":1.10,
        "EUR-UAH":50
}
def trade(user, currency1, currency2, amount):
    if user in r.users:
        try:
            key = f"{currency1}{currency2}"
            price = cost[key]
            r.users[user]["wallet"][currency1] -= amount
            r.users[user]["wallet"][currency2] += amount * price
        except:
            print(user,"додайте гаманець,wallet")
    else:
        print(user, "авторизуйся за допомогою register_user")

def my_wallet(user):
    try:
        print(r.users[user]["wallet"])
    except:
        print(user,"додайте гаманець,wallet")
    else:
        print(user,"авторизуйся за допомогою register_user")