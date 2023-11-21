class Volunteer:
    def __init__(self, name, phone) -> None:
        self.name = name
        self.phone = phone

class Gatepresentation(Volunteer): # Normal inheritance
    def __init__(self, name, phone, warless) -> None:
        self.warless = warless
        super().__init__(name, phone)

class Captain:
    def __init__(self,badge) -> None:
        self.badge = badge

class BodyBuilder(Gatepresentation,Captain): # Multiple inheritance
    def __init__(self,name, phone,warless, badge) -> None:
        Gatepresentation.__init__(self, name, phone, warless)
        Captain.__init__(self, badge)
        
    def __repr__(self) -> str:
        return f'{self.name}, {self.phone}, {self.badge}, {self.warless}'
    
rupa = BodyBuilder('Rupa Begum', 96827534, 'Captain-1', True)
print(rupa)

