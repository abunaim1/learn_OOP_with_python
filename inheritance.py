# base class, parent Class, common attribute + common functionality class
# derived class, child class, uncommon attribute + uncommon functionality class

# learning inheritance with the example of a gadgets shop

# common things class,
class Gadgets:
    def __init__(self, brand, price, color, warranty) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.warranty = warranty

    def term_conditions(self):
        return f'7 days replacement and 2 year parts warranty of all {self.brand}'

class Laptop(Gadgets):
    def __init__(self,brand, price, color, warranty, SSD) -> None:
        self.SSD = SSD
        super().__init__(brand, price, color, warranty)

    def run(self):
        return f'12 gb proccesssor running in this device'
    
    def __repr__(self) -> str:
        return f'Band name: {self.brand}, Price: {self.price}, Color: {self.color}, Warranty: {self.warranty}, SSD type: {self.SSD} And {self.run()}'


class Camera:
    def __init__(self, lense) -> None:
        self.lese = lense
    def focus(self):
        return f'focus you object'

class Phone:
    def __init__(self, display) -> None:
        self.display = display
    def call(self):
        return f'Smooth phone call needed'

asus = Laptop('Asus', 300000, 'Purple', '10 Year', 512)
print(asus)

