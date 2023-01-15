
class Vehicle:
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fill_up_tank(self):
        self.gas = 100

    def empty_tank(self):
        self.gas = 0

    def gas_left(self):
        return self.gas


class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def beep(self):
        print('Beep, beep')


class Truck(Car):
    def __init__(self, price, gas, color, speed, tires):
        super().__init__(price, gas, color, speed)
        self.tires = tires

    def beep(self):
        print('Honk, Honk')


if __name__ == '__main__':

    fef = Truck(1_200, 100, 'blue', 150, '18oz')
    fef.beep()
