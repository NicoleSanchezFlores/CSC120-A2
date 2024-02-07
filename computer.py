class Computer:

    # What attributes will it need?
# We will need a description, a processor type, a hard drive capacity, a memory, and a operating system
    # How will you set up your constructor?
    # We will want to to use class Computerl and use definit(self, description, processor type, hard drive capcity. memory operatingn syste,
    #etc)
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description,
        self.processor_type = processor_type,
        self.hard_drive_capacity = hard_drive_capacity,
        self.memory = memory,
        self.operating_system = operating_system,
        self.year_made = year_made,
        self.price = price

         # You'll remove this when you fill out your constructor
        


    # What methods will you need?
    #we would use a way to change the price, and also a way to change the operting system
    def price_change(self, price):
        self.price = price
    def os_change(self, operating_system):
        self.operating_system = operating_system