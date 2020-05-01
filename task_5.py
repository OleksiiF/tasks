#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""Pattern Abstract Fabric"""

from abc import ABCMeta, abstractmethod


# block of vehicle types
class Vehicle:

    def __init__(self):
        self.passengers = 3
        self.wheels = 4
        self.autopilot = False
        self.fuel = 'gasoline'

    @classmethod
    def get_signal(cls):
        return f"Bib-bib from {cls.__name__}"


class Sedan(Vehicle):
    pass


class Pickup(Vehicle):
    pass


class ElectroSedan(Vehicle):

    def __init__(self):
        super().__init__()
        self.autopilot = True
        self.fuel = 'electricity'


class ElectroPickup(Vehicle):

    def __init__(self):
        super().__init__()
        self.autopilot = True
        self.fuel = 'electricity'


# block of producers
class MainProducer(metaclass=ABCMeta):

    @abstractmethod
    def get_sedan(self) -> Sedan:
        pass

    @abstractmethod
    def get_pickup(self) -> Pickup:
        pass


class Tesla(MainProducer):

    def get_sedan(self) -> ElectroSedan:
        return ElectroSedan()

    def get_pickup(self) -> ElectroPickup:
        return ElectroPickup()


class Audi(MainProducer):

    def get_sedan(self) -> Sedan:
        return Sedan()

    def get_pickup(self) -> Pickup:
        return Pickup()


class Holding:

    def __init__(self):
        self.producers = {
            'tesla': Tesla(),
            'audi': Audi()
        }

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Holding, cls).__new__(cls)

        return cls.instance


def worker():
    holding = Holding()
    producers = [
        producer for producer in holding.producers.values()
    ]
    cars = [ ]
    for prod in producers:
        cars.append(prod.get_sedan())
        cars.append(prod.get_pickup())

    for car in cars:
        print(car.get_signal())


if __name__ == '__main__':
    worker()
