from computer import Computer

class ResaleShop:

    # What attributes will it need?
    # - buying a computer (add to inventory)
    # - selling a computer (remove from inventory)

    # How will you set up your constructor?
    # we can use self

    # Remember: in Python, all constructors have the same name (__init__)
    def __init__(self, inventory):
        self.inventory = inventory

    # What methods will you need? we will use a a way to add a computer using append. And remove a computer will use

    def add_to_inventory(self, computer):
        self.inventory.append(computer)

    def remove_from_inventory(self, computer):
        self.inventory.remove(computer)

    # buy_computer_function, and sell_computer

    # indicates the value of the computer based on its year made
    def refurbish(self, computer: Computer):
        if computer in self.inventory:
            if int(computer.year_made) < 2000:
                computer.price = 0  # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250  # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550  # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000  # recent stuff
        else:
            print("Item not found. Please select another item to refurbish.")

