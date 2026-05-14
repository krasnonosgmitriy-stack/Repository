#n = int(input("enter:"))
#n2 = int(input("enter:"))
#n3 = int(input("enter:"))
#assert n + n2 > n3,"немажліва"

with open("kdsfm.txt", "r") as f:
    x = f.read()
    # перевіряємо, що вміст збігається з тим, що ми записали
    assert x == "sdmv", "Вміст файлу не збігається з очікуваним!"
    print("Файл містить:", x)