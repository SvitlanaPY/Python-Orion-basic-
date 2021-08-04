import time
from random import randint


class NoWater(Exception):
    pass


class FullTrashBin(Exception):
    pass


class BatteryChargeLower20(Exception):
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
            if self.battery_charge > 0:
                self.battery_charge -= Robot.BATTERY_REDUCE
                print("MOVE")
                self.wash()
                self.vacuum_cleaner()
            try:
                if self.battery_charge <= 0:
                    raise NoPower
                if self.battery_charge < 20:
                    raise BatteryChargeLower20
            except BatteryChargeLower20:
                print("Battery charge is lower than 20")
            except NoPower:
                print("NO power! Charge me, please!")

    def wash(self):
        try:
            if self.water <= 0:
                raise NoWater
            else:
                self.water -= Robot.WATER_REDUCE
                print("WASH")
        except NoWater:
            print("NO water! Fill in water tank, please!")

    def vacuum_cleaner(self):
        try:
            if self.trash >= 100:
                raise FullTrashBin
            else:
                self.trash += randint(0, 10)
                print("VACUUM CLEANING")
        except FullTrashBin:
            print("Full trash bin! Clean out, please!")


robot1 = Robot(90, 90, 20)
robot1.move()
