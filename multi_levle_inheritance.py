class Vehicle:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    def __repr__(self) -> str:
        return f'Bus Name: {self.name}'
    def move(self):
        pass

class Bus(Vehicle):
    def __init__(self, name, price, seat) -> None:
        self.seat = seat
        super().__init__(name, price)
    def __repr__(self) -> str:
       
        return f'{self.seat} {super().__repr__()}'
    
class Truck(Vehicle):
    def __init__(self, name, price, weight) -> None:
        self.weight = weight
        super().__init__(name, price)

class PickupTruck(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)

class ACBus(Bus):
    def __init__(self, name, price, seat, temperature) -> None:
        self.temperature = temperature
        super().__init__(name, price, seat)
    def __repr__(self) -> str:
        print(f'Bus Price: {self.price} Bus Temperature: {self.temperature}')
        return super().__repr__()

ena = ACBus('ENA', 48397250239085723, 22, 34)
print(ena)