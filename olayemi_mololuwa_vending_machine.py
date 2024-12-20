class VendingMachine:
    def __init__(self, soda, coffee, water):
        self.soda = soda
        self.coffee = coffee
        self. water = water
    def buy(self):
        option = int(input(f'Please select an option:\n1 - Soda\n2 - Coffee\n3 - Water\n:> '))
        if option == 1:
            self.soda = self.soda + 1
        elif option == 2:
            self.coffee = self.coffee + 1
        elif option == 3:
            self.water = self.water + 1
    def restock(self):
        option = int(input(f'Please select an option:\n1 - Soda\n2 - Coffee\n3 - Water\n:> '))
        amount = int(input("Please enter an amount: "))
        if option == 1:
            self.soda = self.soda + amount
        elif option == 2:
            self.coffee = self.coffee + amount
        elif option == 3:
            self.water = self.water + amount

    def inventory(self):
        print(f'Inventory\nSoda: {self.soda} bottles\nCoffee: {self.coffee} bottles\nWater: {self.water} bottles\n')
Vendor_1 = VendingMachine(8,10,10)    
while True:
    command = input(":> ")
    if command == "buy":
        Vendor_1.buy()
    elif command == "restock":
        Vendor_1.restock()
    elif command == "inventory":
        Vendor_1.inventory()
    elif command == "quit" or command == "q":
        break
    else:
        print("Please Enter Valid Command ('buy', 'restock','inventory', or 'quit')")
