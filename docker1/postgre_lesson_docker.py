import psycopg2

conn = psycopg2.connect(
    dbname="products",
    user="admin",
    password="secretpassword",
    host="postgres",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM products;")
rows = cursor.fetchall()

print("Список товарів:")
print("-" * 50)
for row in rows:
    id_, name, price, quantity = row
    print(f"ID: {id_} | Назва: {name} | Ціна: {price} грн | Кількість: {quantity} шт.")

conn.close()