"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""


class Clothes:
    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        pass

    def __add__(self, other):
        return f"Необходимый расход ткани для пошива: {self.param / 6.5 + 0.5 + 2 * other.param + 0.3 :.2f} м"


class Coat(Clothes):
    @property
    def consumption(self):
        return f"Расход ткани для пошива пальто составил: {self.param / 6.5 + 0.5 :.2f} м"


class Costume(Clothes):
    @property
    def consumption(self):
        return f"Расход ткани для пошива костюма составил: {2 * self.param + 0.3 :.2f} м"


coat = Coat(200)
costume = Costume(100)
print(coat.consumption)
print(costume.consumption)
print(coat + costume)