class Account:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance



class Bank:
    
    def __init__(self, mojodi, ramz_malom, ramz):
        self.mojodi = mojodi
        self.ramz_malom = ramz_malom
        self._ramz = ramz
        self.__priverNum = 132
    
    def show(self):
        return self.ramz_malom

    def _show_protect_ramz_(self):
        return self.ramz_malom
    
    def __show_privet_ramz(self):
        return self.ramz_malom
    

b1 = Bank(1000, 123, 789)
print("Public Value: ", b1.mojodi)
print("Protect Value: ", b1._ramz)
print("Private Value: ", b1._Bank__priverNum)

print("Public Method: ", b1.show())
print("Protect Method: ",b1._show_protect_ramz_())
print("Private Method: ",b1._Bank__show_privet_ramz())
