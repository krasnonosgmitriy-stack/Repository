#class Remote_TV:
#    def __init__(self,color,number_of_buttons,
#superpower):
#        self.color = color
#        self.number_of_buttons = number_of_buttons
#        self.superpower = superpower

#    def biba(self):
#        print(f"цей пульт має {self.color} колір, має таку кількість кнопок {self.number_of_buttons}, та має здатнисть {self.superpower}#")

#    def knopka(self):
#        if self.number_of_buttons > 40:
#            print("пульт крутий")
#        else:
#            print("поганий пульт")

#x = Remote_TV("червоний",46,"віддалене керування")
#x.biba()
#x.knopka()

#class ShoppingCart:
#    def __init__(self):
#        self._items = []          # protected
#        self.__total_price = 0   # private
#
#    def add_item(self, name, price):
#        self._items.append((name, price))
#        self.__total_price += price
#
#    def remove_item(self, name):
#        for item in self._items:
#            if item[0] == name:
#                self._items.remove(item)
#                self.__total_price -= item[1]
#                break
#
#    def get_total(self):
#        return self.__total_price
#
#    def apply_discount(self, percent):
#        discount = self.__total_price * (percent / 100)
#        self.__total_price -= discount
#
#
#cart = ShoppingCart()
#cart.add_item("Хліб", 30)
#cart.add_item("Молоко", 45)
#
#print(cart.get_total())
#
#cart.apply_discount(10)
#print(cart.get_total())
#
#cart.remove_item("Хліб")
#print(cart.get_total())

#class Employee:
#    def __init__(self, name, salary, department):
#        self.name = name
#        self._salary = salary
#        self.__department = department
#
#    def get_salary(self):
#        return self._salary
#
#    def set_salary(self, salary):
#        if salary >= self._salary:
#            self._salary = salary
#
#    def get_department(self):
#        return self.__department
#
#    def set_department(self, department):
#        self.__department = department
#
#class Shape:
#    def area(self):
#        return 0
#
#class Rectangle(Shape):
#    def __init__(self, a, b):
#        self.a = a
#        self.b = b
#
#    def area(self):
#        return self.a * self.b
#
#class Circle(Shape):
#    def __init__(self, r):
#        self.r = r
#
#    def area(self):
#        return 3.14 * (self.r ** 2)
#
#
#rect = Rectangle(5, 4)
#circle = Circle(3)
#
#print(rect.area())
#print(circle.area())
#
#from abc import ABC, abstractmethod
#
#class Automiyka(ABC):
#    @abstractmethod
#    def wash(self):
#        pass
#
#class Vantazhivka(Automiyka):
#    def wash(self):
#        print("Миємо вантажівку")
#
#class Legkova(Automiyka):
#    def wash(self):
#        print("Миємо легкове авто")
#
#class Moto(Automiyka):
#    def wash(self):
#        print("Миємо мотоцикл")
#
#Vantazhivka().wash()
#Legkova().wash()
#Moto().wash()

#from abc import ABC, abstractmethod
#
#class Shape(ABC):
#    @abstractmethod
#    def calculate_area(self):
#        pass
#
#class Triangle(Shape):
#    def calculate_area(self):
#        return "S = 1/2 * a * h"
#
#class Rectangle(Shape):
#    def calculate_area(self):
#        return "S = A * B"
#
#class Circle(Shape):
#    def calculate_area(self):
#        return "S = π * r²"
#
#classes = [Triangle(), Rectangle(), Circle()]
#
#for c in classes:
#    print(c.calculate_area())
import asyncio
from aiogram import Bot, Dispatcher, html
from aiogram.filters import CommandStart, Command
from config import BOT_TOKEN
from aiogram.types import Message
dp = Dispatcher()

@dp.message(CommandStart())
async def Start(message: Message):
    await message.answer(f"Hello {message.from_user.full_name}!")

@dp.message(Command("help"))
async def Help_handler(message: Message):
    await message.answer("че хочешь мудила")

@dp.message(Command("send_movie"))
async def Help_handler(message: Message):
    await message.answer("пшел нах")

@dp.message()
async def Start_1(message: Message):
    await message.send_copy(chat_id=message.chat.id)

async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())