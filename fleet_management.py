# Ena Poribahan

class Company:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.bus = []
        self.routes = []
        self.driver = []
        self.counter = []
        self.supervisor = []
        self.fare = []

class Driver:
    def __init__(self, name, license, location, age, exprience) -> None:
        self.name = name
        self.license = license
        self.location = location
        self.age = age
        self.exprience = exprience

class Counter:
    def __init__(self) -> None:
        pass

class Passenger:
    def __init__(self) -> None:
        pass

class Supervisor:
    def __init__(self) -> None:
        pass

# class --> object banacchi

ena = Company('Ena Poribahan', "Dhaka-12001")