# encapsulation = hide details
# access modifier = public, protected, private
class Bank:
    def __init__(self, holder_name, initial_deposite) -> None:
        self.holder_name = holder_name # public attribute
        self.__balance = initial_deposite # private attribute
        self._branch = 'banani 11' # protected attribute
    
    def deposite(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
        
    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            return amount
        else:
            return f'Fokira bhaiya'

rafsan = Bank('Choto Bhai', 10000)
rafsan.deposite(560000)
print(rafsan.get_balance())        
print(rafsan.withdraw(5600000000000))
print(rafsan.get_balance())
rafsan.holder_name = 'boro bhai'
print(rafsan.holder_name)

# print(rafsan._branch)

print(rafsan._Bank__balance) # accessing a private member with Name Mangling