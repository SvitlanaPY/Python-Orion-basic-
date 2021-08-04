import time
from random import randint


class NoWater(Exception):
    pass

class FullTrashBin(Exception):
    pass

class ChargeLower20(Exception):
    pass

class NoPower(Exception):
    pass


class Robot:
    WATER_REDUCE = 10
    BATTERY_REDUCE = 10

    def __init__(self, battery_charge, trash, water):
        self.battery_charge = battery_charge
        self.trash = trash
        self.water = water


    def move(self):
        while True:
            time.sleep(1)
            print("MOVE")
            self.battery_charge = self.battery_charge - Robot.BATTERY_REDUCE
            self.wash()
            self.vacuum_cleaner()


    def wash(self):
        try:
            if self.water <= 0:
                raise NoWater
            else:
                self.water = self.water - Robot.WATER_REDUCE
                print("WASH")
        except NoWater:
            print("NO water! Fill in water tank, please!")


    def vacuum_cleaner(self):
        try:
            if self.trash >= 99:
                raise FullTrashBin
            else:
                self.trash = self.trash + randint(0, 10)
                print("VACUUM CLEANING")
        except FullTrashBin:
            print("Full trash bin! Clean out, please!")


robot1 = Robot(90, 90, 20)
robot1.move()
