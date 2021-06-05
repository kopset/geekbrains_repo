from datetime import datetime
from time import sleep


class PlaneCabin:
    _max_cnt = 1
    __current_cnt = 0

    __auth = {"secret": "Nikolai Sviridov",
              "some pass": "Vladislav Makeev"}

    def __init__(self, capacity, extra_places):
        self._capacity = capacity
        self.extra_places = extra_places
        self.current_free_places = self._capacity
        PlaneCabin.__current_cnt += 1

    def make_reservation(self, num):
        if num > self.current_free_places:
            raise ValueError(f"Overbooking Error!!! Current free places value is {self.current_free_places}")
        self.current_free_places -= num

    @property
    def succeed_koef(self):
        sleep(5)
        return (self._capacity + self.extra_places - self.current_free_places) /\
               (self._capacity + self.extra_places)

    def __check_value_to_be_unbooked(self, num):
        if num + self.current_free_places > self._capacity:
            raise ValueError("Smth went wrong! You try to free more palces, than you have in this plane!")

    def undo_reservation(self, num):
        self.__check_value_to_be_unbooked(num)
        self.current_free_places += num

    def get_max_cnt(self):
        return PlaneCabin._max_cnt

    def get_current_cnt(self, password):
        if password in PlaneCabin.__auth:
            with open("access_log.txt", "a") as log:
                log.write(f"{datetime.now()}: {PlaneCabin.__auth[password]}\n")
            print("ПРОИЗОШЕЛ ДОСТУП К ПРИВАТНОМУ ПАРАМЕТРУ! ДЕЛАЮ ЗАПИСЬ В БАЗУ")
            return PlaneCabin.__current_cnt
        else:
            raise ValueError("Неверный пароль!")

    def __repr__(self):
        return f"Capacity: {self._capacity}\nFree places: {self.current_free_places}\nExtra: {self.extra_places}"

    def __str__(self):
        return f"Capacity: {self._capacity}\nFree places: {self.current_free_places}\nExtra: {self.extra_places}"

    def __add__(self, other):
        capacity = self._capacity + other._capacity
        extra = self.extra_places + other.extra_places
        return PlaneCabin(capacity, extra)

    def __mul__(self, other):
        pass

    def __iter__(self):
        yield {"name": "capacity", "value": self._capacity}
        yield {"name": "extra_places", "value": self.extra_places}
        yield {"name": "current_free_places", "value": self.current_free_places}

    def __eq__(self, other):
        return (self.extra_places == other.extra_places) and (self._capacity == other._capacity)

klm = PlaneCabin(10, 2)
c = 2
# klm.get_current_cnt("secret")
# klm.get_current_cnt("some pass")
# klm.get_current_cnt("secret")
# klm.get_current_cnt("some pass")
# klm.get_current_cnt("secret")
# klm.get_current_cnt("some pass")



# lufthanza = PlaneCabin(10, 2)
# print(id(klm), id(lufthanza), klm == lufthanza)
# turkish_airlines = PlaneCabin(7, 5)
# common_cabin = klm + lufthanza + turkish_airlines
# print(common_cabin)

# klm_iterator = iter(klm)
# print(klm_iterator)

# for field in klm:
#     print(field)
#
#
# l = [1, 2, 3]
# print(iter(l))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for el in l:
#     print(l)

# iterator = iter(l)
# try:
#     while True:
#         print(next(iterator))
# except StopIteration as err:
#     print("итерация завершена")


# class SlaboyeZveno:
#     def __init__(self):
#         self.start_priz = 0
#         self.finish_priz = 10_000
#
#     def __iter__(self):
#         return SlaboyeZvenoIterator(self.start_priz, self.finish_priz, 1000)
#
#
# class SlaboyeZvenoIterator:
#     def __init__(self, start, finish, step):
#         self.start = start
#         self.finish = finish
#         self.step = step
#         self.current_value = self.start
#
#     def __next__(self):
#         if self.current_value < self.finish:
#             self.current_value += self.step
#             return self.current_value
#         else:
#             raise StopIteration("Итерация завершена!")
#
#     def to_start(self):
#         self.current_value = 0
#
#     def to_value(self, value):
#         self.current_value = value
#
#     def __iter__(self):
#         return self
#
#
# from time import sleep
#
# sl_z = SlaboyeZveno()
# iterator = iter(sl_z)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# iterator.to_start()
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))





from typing import List
from time import sleep
from datetime import datetime
import requests
from abc import ABC, abstractmethod

from lesson_6.cw_6 import Pistolet


class MyShinyIterator:
    def __init__(self, finish):
        self.i = 0
        self.finish = finish
    #     self.buf = self.i

    def __next__(self):
        self.i += 1
        if self.i <= self.finish:
            return self.i
        else:
            raise StopIteration("Итерация окончена")

    def to_start(self):
        self.i = 0

    def __iter__(self):
        return self


class CustomClass:
    def __iter__(self):
        return MyShinyIterator(3)

#
# cc = CustomClass()
#
# it = iter(cc)
#
# print(next(it))
# print(next(it))
# it.to_start()
# print(next(it))
# print(next(it))




class Point2D:
    """Двумерная точка"""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"координата x: {self.x}, координата y: {self.y}"

    def __repr__(self):
        return f"координата x: {self.x}, координата y: {self.y}"

    def __add__(self, other):
        new_coord_x = self.x + other.x
        new_coord_y = self.y + other.y
        return Point2D(new_coord_x, new_coord_y)

    def __mul__(self, other):
        if type(other) == Point2D:
            return Point2D(self.x * other.x, self.y * other.y)
        elif type(other) == int:
            return Point2D(self.x * other, self.y * other)
        raise ValueError("Unsupported type for mult: ", type(other))

    def __eq__(self, other):
        return True if self.x is other.x and self.y is other.y else False

    def __iter__(self):
        return MyShinyIterator(self)
    # def __iadd__(self, other):
    #     self.x += other.x
    #     self.y += other.y

    @property
    def get_very_hard_evaluation(self):
        return self.y + self.x
    #
    # def test(self, *args, **kwargs):
    #     pass


# point_2d = Point2D(100000, 2)
# c = 1

class MClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# m_class_ex = MClass(100000, 2)
# point_2d = Point2D(100000, 2)
# point_2d_2 = Point2D(100000, 2)
# # print(m_class_ex == point_2d)
# print(sum([point_2d_2, point_2d]))








class AllPointHeap:
    def __init__(self, point_1: Point2D, point_2: Point2D):
        self.point_1 = point_1
        self.point_2 = point_2

    def get_sum_sum_coor(self):
        return self.point_1.get_very_hard_evaluation + self.point_2.get_very_hard_evaluation


class Test:
    def __init__(self):
        self.field = None

    def test_method(self):
        self.field = Point2D(1, 2)

# tobj = Test()
# tobj.test_method()
# c = 1


class Point3D(Point2D):
    """Трёхмерная точка"""
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return f"{super().__str__()}, координата z: {self.z}"

    def __eq__(self, other):
        if not super().__eq__(other):
            return False
        return True if self.z == other.z else False

    def __add__(self, other):
        c = 1
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)


# point_3 = AllPointHeap(point_2d, point_1d)

# print(point_3.get_sum_sum_coor())
#
#
# point_3d = Point3D(1, 2, 3)
# point_3d2 = Point3D(4, 2, 3)
# new_p = point_3d + point_3d2 + point_3d2 + point_3d2 + point_3d2 + point_3d2 + point_3d2
# c = 1
# point_3d = Point3D(1, 2, 3)
# print(point_2d)

# print(point_3d == point_3d2)


class Animal(ABC):
    @abstractmethod
    def feed(self):
        pass

    def voice(self):
        pass


class Dog(Animal):
    def feed(self):
        print("Меня кормят")


class Oter(Dog):
    def voice(self):
        print("Гав")

    def dance(self):
        print("Я танцую")


class User:
    def __init__(self, field):
        self.field = field

    def get_discount_status(self):
        sleep(2)
        return requests.get("https://google.com")

user = User(123)
c = 1

###################################
############ ИТЕРАТОРЫ ############
###################################

import sys
from itertools import repeat, count

# Итерируемые объекты (iterable) — это любые объекты, предоставляющий возможность поочерёдного прохода по циклу.
from time import sleep

# my_list = [1, 2, 3]
# c = iter(range(10))
# my_dict = {1: "a", 2: "b", 3: "c"}
# my_set = {"lol", "kek", "cheburek"}

# point_2d = Point2D(100000, 2)
# i = iter(point_2d)
# try:
#     while True:
#         print(next(i))
# except StopIteration as err:
#     pass


def simple_gen(start, finish=5):
    while start <= finish:
        yield start
        start += 1


# простая петля
# for element in point_2d:
#     print(element)

# iterator = iter(my_list)
# print(next(my_list))  # упадёт ошибка
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# numbers = [1, 2, 3, 4, 5, 6]
# squares = (n**2 for n in numbers)
# print(9 in squares)
# print(9 in squares)
# print(next(squares))


class TumbCollection:
    """
    Объект, поддерживающий интерфейс итерации (итерируемый объект)
    """
    def __init__(self, start):
        self.start = start - 1

    def __iter__(self):
        c = 1
        # Метод __iter__ должен возвращать объект-итератор (генератор - это подвид итератора)
        return simple_gen(self.start)


# Ключевой вопрос - что можно итерировать? Ответ - то, что реализует интерфейс итерации.
# obj = TumbCollection(start=1)
# for el in obj:
#     print(el)
# print("тумб второй проход")
# for el in obj:
#     print(el)
#
# print("************")
# it = MyShinyIterator(start=2)
# for el in it:
#     print(el)
# print("второй проход")
# for el in it:
#     print(el)
# print("третий проход")
# for el in it:
#     print(el)

# gen = simple_gen(5, 7)
# for x in gen:
#     print(x)
# for x in gen:
#     print(x)
# for x in gen:
#     print(x)
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())


class SquareAll:
    def __init__(self, numbers):
        self.numbers = iter(numbers)

    def __next__(self):
        return next(self.numbers) ** 2

    def __iter__(self):
        return self


# numbers = [1, 2, 3, 4, 5]
#
#
# def square_all(numbers):
#     for n in numbers:
#         yield n**2


# square_all_ex = (n**2 for n in numbers)
# print(9 in square_all_ex)
# print([x for x in square_all_ex])
# print(9 in square_all_ex)


# как мы экономим память
# lots_of_fours = repeat(4, times=100_000_000)
# print(type(lots_of_fours))
# print(f"lots_of_fours занимает в памяти {sys.getsizeof(lots_of_fours)} байт")

# lots_of_fours_via_list = [4] * 1_000_000_000  # 8000000064
# print(f"lots_of_fours занимает в памяти {sys.getsizeof(lots_of_fours_via_list)} байт")

def rr():
    n = 0
    while n <= 10:
        yield n
        n += 1


l = rr()
print(5 in l)
for el in l:
    print(el)

# бесконечно длинный итератор
# for n in count():
#     print(n)
#     sleep(1)