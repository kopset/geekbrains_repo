from random import randint


class Auto:
    material = 'steel'
    secret_model_id = 12345

    def __init__(self, color, engine_power):
        self.color = color
        self.engine_power = engine_power
        self.is_on = False
        self.secret_number = randint(0, 100_000_000)

    def gas(self):
        if not self.is_on:
            print("You have to switch on your car!")
            return
        print(f"Auto with color {self.color} and material {Auto.material} and engine power"
              f" {self.engine_power} make Wruuuuuuummmmmmm")

    def switch_on(self):
        if self.is_on:
            print("Auto has been switched on yet!")
            return
        self.is_on = True

    def switch_off(self):
        if not self.is_on:
            print("Auto has been switched off yet!")
            return
        self.is_on = False

    def info(self):
        print(f"{self.color}, {self.engine_power}")


class WarAuto(Auto):
    def __init__(self, color, engine_power, weapon_type):
        super().__init__(color, engine_power)
        self.weapon_type = weapon_type

    def shoot(self):
        print("Fire!!!!")

    def gas(self):
        super().gas()
        print("I make noise by my machinegun!")


class MedicineAuto(Auto):
    def heal_somebody(self):
        print("heal!")

    def gas(self):
        super().gas()
        print("I AM HEAL MACHINE!")


class MedWarCar(WarAuto, MedicineAuto):
    pass


# my_shiny_auto = Auto('red', 100)
# my_shiny_auto2 = Auto('blue', 200)
# my_shiny_auto3 = Auto('black', 300)
# print(Auto.material)
# print(my_shiny_auto.material)
# print(Auto._Auto__secret_model_id)
# my_shiny_auto.gas()
# my_shiny_auto2.gas()
# my_shiny_auto3.gas()
# print(my_shiny_auto.__is_on)
# my_shiny_auto.switch_on()
# my_shiny_auto.switch_on()
# print(my_shiny_auto.is_on)
war_car = WarAuto('red', 100, 'pistol')
med_war_car = MedWarCar('red', 100, 'pistol')
# med_war_car.heal_somebody()
med_war_car.gas()
# medicine_car = MedicineAuto('red', 100)
# war_car.switch_on()
# medicine_car.switch_on()
# war_car.shoot()
# war_car.gas()

class Pistolet:

    def __init__(self, weight, max_capacity, color):
        self.weight = weight
        self.color = color
        self.max_capacity = max_capacity

    def __new__(cls, *args, **kwargs):
        c = 1

    def __call__(self, *args, **kwargs):
        print(self._shoot())

    def _shoot(self):
        return "ОГОНЬ НА ПОРАЖЕНИЕ!"


p = Pistolet(123, 123, 'red')


class Automat:
    def __init__(self, bps):
        self.bps = bps

    def _shoot(self):
        return "АВТОМАТИЧЕСКИЙ ОГОНЬ НА ПОРАЖЕНИЕ!"


class ToyPistol(Pistolet):
    def __init__(self, new_field, weight, max_capacity, color):
        super().__init__(weight, max_capacity, color)
        self.new_field = new_field

    def _shoot(self):
        print(super()._shoot())
        return "АВТОМАТИЧЕСКИЙ ОГОНЬ НА ПОРАЖЕНИЕ!"

# toy_pistol = ToyPistol("water", 1, 12, "water")
# toy_pistol()

class Plane:
    _max_cnt = 1
    __current_cnt = 0

    def __init__(self, capacity):
        if Plane.__current_cnt == Plane._max_cnt:
            raise ValueError("Max number of plane is reached! Please sell it or do smth!")
        self._capacity = capacity
        self.current_free_places = self._capacity
        Plane.__current_cnt += 1

    def make_reservation(self, num):
        if num > self.current_free_places:
            raise ValueError(f"Overbooking Error!!! Current free places value is {self.current_free_places}")
        self.current_free_places -= num

    def __check_value_to_be_unbooked(self, num):
        if num + self.current_free_places > self._capacity:
            raise ValueError("Smth went wrong! You try to free more palces, than you have in this plane!")

    def undo_reservation(self, num):
        self.__check_value_to_be_unbooked(num)
        self.current_free_places += num

    def get_max_cnt(self):
        return Plane._max_cnt


class WarehousePlane(Plane):
    def __init__(self, capacity, stuff_capacity):
        super().__init__(capacity)
        self.stuff_capacity = stuff_capacity

    def shoot(self):
        print("ЧТо-то делаю!!!")

    def make_reservation(self, num):
        if num > 3:
            super().make_reservation(num)
        else:
            raise ValueError("Error due to booking")


class Weapon:
    def shoot(self):
        print("Я стреляю!!!")


class MilitaryPlane(WarehousePlane, Weapon):
    pass



# def func():
#     pass

plane_1 = WarehousePlane(10, 100)
plane_1.make_reservation(5, 1)
plane_1.undo_reservation(3)
print(plane_1.current_free_places)
# print(plane_3.current_free_places)
# plane_3.make_reservation(10)
# print(plane_3.current_free_places)
# plane_3.undo_reservation(5)
# print(plane_3.current_free_places)