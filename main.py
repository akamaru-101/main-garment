class Garment:
    def __init__(self, name=""):
        self.name = name

    def calculate_price(self):
        raise NotImplementedError

    def set_collar_size(self, cs):
        pass

    def get_collar_size(self):
        return 0

    def set_waist(self, w):
        pass

    def get_waist(self):
        return 0

    def show(self):
        pass

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Upper(Garment):
    def __init__(self, name=""):
        super().__init__(name)
        self.collar_size = 0

    def get_collar_size(self):
        raise NotImplementedError

    def set_collar_size(self, cs):
        self.collar_size = cs

    def get_collar_size_value(self):
        return self.collar_size

class Lower(Garment):
    def __init__(self, name=""):
        super().__init__(name)
        self.waist = 0

    def get_waist(self):
        raise NotImplementedError

    def set_waist(self, w):
        self.waist = w

    def get_waist_value(self):
        return self.waist

class Shirt(Upper):
    def __init__(self, name=""):
        super().__init__(name)
        self.price = 0

    def get_collar_size(self):
        return self.get_collar_size_value()

    def calculate_price(self):
        self.price = (self.get_collar_size() - 1) * 20 + 10
        return self.price

    def show(self):
        print("---Shirt---")
        print(f"The collar size for your shirt is: {self.get_collar_size()}")
        print(f"The price of the shirt is: {self.calculate_price()}")

class Pajama(Lower):
    def __init__(self, name=""):
        super().__init__(name)
        self.price = 0

    def get_waist(self):
        return self.get_waist_value()

    def calculate_price(self):
        self.price = (self.get_waist() - 2) * 15 + 50
        return self.price

    def show(self):
        print("---Pajama---")
        print(f"The waist size for your pajama is: {self.get_waist()}")
        print(f"The price of the pajama is: {self.calculate_price()}")

class Trouser(Lower):
    def __init__(self, name=""):
        super().__init__(name)
        self.price = 0

    def get_waist(self):
        return self.get_waist_value()

    def calculate_price(self):
        self.price = (self.get_waist() - 3) * 20 + 100
        return self.price

    def show(self):
        print("---Trouser---")
        print(f"The waist size for your trouser is: {self.get_waist()}")
        print(f"The price of the trouser is: {self.calculate_price()}")

def show_menu():
    print("Enter 1 : Add an Item to the shopping cart")
    print("Enter 2 : Remove an Item from the shopping cart")
    print("Enter 3 : Show Shopping Cart")
    print("Enter 4 : Make the payment")

def main():
    print("                                ----Welcome to the Garment Store----\n")
    cart = []

    total_price = 0

    while True:
        show_menu()
        choice = int(input("\nEnter your choice: "))
        print()

        if choice == 1:
            if len(cart) < 10:
                print("Available items are:")
                print("Enter 1 : Shirt")
                print("Enter 2 : Pajama")
                print("Enter 3 : Trouser")
                choice2 = int(input("\nEnter your choice: "))
                print()

                if choice2 == 1:
                    collar_size = int(input("Enter the collar size for the shirt: "))
                    item = Shirt()
                    item.set_collar_size(collar_size)
                    cart.append(item)
                    print("\nShirt is successfully added to the cart\n")
                    total_price += item.calculate_price()
                    item.show()
                    print()

                elif choice2 == 2:
                    waist_size = int(input("Enter the waist size for the pajama: "))
                    item = Pajama()
                    item.set_waist(waist_size)
                    cart.append(item)
                    print("\nPajama is successfully added to the cart\n")
                    total_price += item.calculate_price()
                    item.show()
                    print()

                elif choice2 == 3:
                    waist_size = int(input("Enter the waist size for the trouser: "))
                    item = Trouser()
                    item.set_waist(waist_size)
                    cart.append(item)
                    print("\nTrouser is successfully added to the cart\n")
                    total_price += item.calculate_price()
                    item.show()
                    print()

            else:
                print("You have added the maximum items in your cart\n")

        elif choice == 2:
            if cart:
                print("                      ----Your Shopping Cart----\n")
                print(f"Number of items in the cart: {len(cart)}\n")

                for index, item in enumerate(cart, start=1):
                    print(f"{index} ", end="")
                    item.show()
                    print()

                print(f"Your Total Bill is {total_price}\n")

                remove = int(input("Enter the item number you want to remove: "))
                print()
                if 1 <= remove <= len(cart):
                    print(f"Item Number {remove} has been removed successfully\n")
                    total_price -= cart[remove - 1].calculate_price()
                    del cart[remove - 1]
                else:
                    print("Invalid Item Number")
                    print("Please enter a valid Item Number to remove\n")

            else:
                print("Your Shopping Cart is Empty")
                print("Please add some items to the cart\n")

        elif choice == 3:
            if cart:
                print("                      ----Your Shopping Cart----\n")
                print(f"Number of items in the cart: {len(cart)}\n")

                for index, item in enumerate(cart, start=1):
                    print(f"{index} ", end="")
                    item.show()
                    print()

                print(f"Your Total Bill is {total_price}\n")

            else:
                print("Your Shopping Cart is Empty")
                print("Please add some items to the cart\n")

        elif choice == 4:
            if cart:
                print(f"Your Total Bill is {total_price}\n")
                print("Payment Made Successfully")
                print("Thank you for shopping at our store\n")
                break

            else:
                print("Your Shopping Cart is Empty")
                print("Please add some items to the cart\n")

        else:
            print("Please Enter a valid choice\n")

if __name__ == "__main__":
    main()
