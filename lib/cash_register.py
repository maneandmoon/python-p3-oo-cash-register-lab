#!/usr/bin/env python3
import ipdb
#  We're going to create an Object-Oriented Cash Register that can:

# - Add items of varying quantities and prices
# - Calculate discounts
# - Keep track of what's been added to it
# - Void the last transaction

# Step 1: Create the CashRegister Class
# 1.	Initialize the Class:
# The class should initialize with an optional discount parameter.
# Set the total to 0.
# Initialize items as an empty list.

# 2.	Add Items:
# Method to add items to the register.
# The method should accept title, price, and an optional quantity.

# 3.	Apply Discount:
# Method to apply the discount to the total.

# 4.	Void Last Transaction:
# Method to void the last transaction.

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.00
        self.items = []
        self.last_transaction = 0.0

        #self. are attributes 
       # .add_item(has parameters)


    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        # self.items.append([title] * quantity)
        self.items.extend([title] * quantity)
        #.append or .extend?
        self.last_transaction = price * quantity

 # **Hint #2:** The `apply_discount()` method requires some knowledge about working with integers versus floats in Python. When you get to that method, take a look at what return value the tests are expecting and keep in mind that Python provides methods for changing an Integer to a Float and vice versa.        

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total  #float /100
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")  #convert to int
        else:
            print("There is no discount to apply.")


# **Hint #3:** The `void_last_transaction()` method will remove the last
# transaction from the total. You'll need to make an additional attribute and keep
# track of that last transaction amount somehow. In what method of the class are
# you working with an individual item?            

    def void_last_transaction(self):
    #     def test_void_last_transaction(self):
    #   '''subtracts the last item from the total'''
        self.total -= self.last_transaction

    #     def test_void_last_transaction_with_multiples(self):
    #   '''returns the total to 0.0 if all items have been removed'''
        self.last_transaction = 0.0

# **Hint #4:** Python handles mutable default values for arguments differently
# than it handles immutable default values. This means that you should usually not
# set default values for lists, dictionaries, and instances of classes. You can
# learn more on this quirk in Python's documentation on [More Control Flow Tools
# ](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values).





# CashRegister in cash_register.py takes one optional argument, a discount, on initialization. .                                                                                                                                                [  7%]
# CashRegister in cash_register.py sets an instance variable total to zero on initialization. .                                                                                                                                                 [ 14%]
# CashRegister in cash_register.py sets an instance variable items to empty list on initialization. .                                                                                                                                           [ 21%]
# CashRegister in cash_register.py accepts a title and a price and increases the total. .                                                                                                                                                       [ 28%]
# CashRegister in cash_register.py also accepts an optional quantity. .                                                                                                                                                                         [ 35%]
# CashRegister in cash_register.py doesn"t forget about the previous total .                                                                                                                                                                    [ 42%]
# CashRegister in cash_register.py applies the discount to the total price. .                                                                                                                                                                   [ 50%]
# CashRegister in cash_register.py prints success message with updated total .                                                                                                                                                                  [ 57%]
# CashRegister in cash_register.py reduces the total .                                                                                                                                                                                          [ 64%]
# CashRegister in cash_register.py prints a string error message that there is no discount to apply .                                                                                                                                           [ 71%]
# CashRegister in cash_register.py returns an array containing all items that have been added .                                                                                                                                                 [ 78%]
# CashRegister in cash_register.py returns an array containing all items that have been added, including multiples .                                                                                                                            [ 85%]
# CashRegister in cash_register.py subtracts the last item from the total .                                                                                                                                                                     [ 92%]
# CashRegister in cash_register.py returns the total to 0.0 if all items have been removed .

# ipdb.set_trace()

        