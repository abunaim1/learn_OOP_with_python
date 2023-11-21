class Book:
    def __init__(self, name) -> None:
        self.name = name
    def read(self):
        raise NotImplementedError

class Physics(Book):
    def __init__(self, name) -> None:
        super().__init__(name)
    def read(self):
        return f'Good one'

class Chemistry:
    def __init__(self) -> None:
        pass

topon = Physics('Topon')
print(topon.read())

print(issubclass(Physics, Book))
print(issubclass(Chemistry, Book))
print(isinstance(topon,Book))
    