class Account:
    def __init__(self,name:str,balance:int):
        self.name = name
        self.balance = balance
        
    def display_balance(self) -> None:
        print(f"Balance: ${self.balance}")


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
