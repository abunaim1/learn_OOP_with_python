from abc import ABC, abstractmethod
#abstract base class

class Animal(ABC):
    def __init__(self) -> None:
        pass
    @abstractmethod #enforce all derived class to have a eat method
    def eat(self):
        pass
    def move(self):
        pass
    @abstractmethod
    def run(self):
        print('Runing is the best thing for human')

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.name = name
        super().__init__()
    def eat(self):
        print("Hay nanan, eating banananaa")
    def run(self):
        print('But i am monkey here')

layka = Monkey('Laok afa krumchan')
layka.eat()
layka.run()

       
    

