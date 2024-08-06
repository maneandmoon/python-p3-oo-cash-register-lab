#!/usr/bin/env python3

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


    # cash_register = CashRegister()
    # cash_register_with_discount = CashRegister(20)

# **This is a test-driven lab!** You will need to read the spec file and the test
# output very carefully to solve this one.

# Note that a **discount** is calculated as a percentage off of the total cash
# register price (e.g. a discount of 20 means the customer receives 20% off of
# their total price).

# **Hint #1:** Keep in mind that to access an attribute or call an instance method
# _inside_ another instance method, we use the `self` keyword to refer to the
# instance on which we are operating.

# class CashRegister:
#     def __init__(self, discount=0):
        

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    # def reset_register_totals(self):
    #   self.cash_register.total = 0
    #   self.cash_register_with_discount.total = 0

    # def test_discount_attribute(self):
    #     '''takes one optional argument, a discount, on initialization.'''
    #     assert(self.cash_register.discount == 0)
    #     assert(self.cash_register_with_discount.discount == 20)

    # def test_total_attribute(self):
    #     '''sets an instance variable total to zero on initialization.'''
    #     assert(self.cash_register.total == 0)
    #     assert(self.cash_register_with_discount.total == 0)

    # def test_items_attribute(self):
    #     '''sets an instance variable items to empty list on initialization.'''
    #     assert(self.cash_register.items == [])
    #     assert(self.cash_register_with_discount.items == [])

  
    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = price * quantity

    # def test_add_item(self):
    #     '''accepts a title and a price and increases the total.'''
    #     self.cash_register.add_item("eggs", 0.98)
    #     assert(self.cash_register.total == 0.98)
    #     # self.reset_total(self.cash_register)
    #     self.reset_register_totals()

    # def test_add_item_optional_quantity(self):
    #     '''also accepts an optional quantity.'''
    #     self.cash_register.add_item("book", 5.00, 3)
    #     assert(self.cash_register.total == 15.00)
    #     # self.cash_register.total = 0
    #     self.reset_register_totals()

    # def test_add_item_with_multiple_items(self):
    #     '''doesn"t forget about the previous total'''
    #     self.cash_register.add_item("Lucky Charms", 4.5)
    #     assert(self.cash_register.total == 4.5)
    #     self.cash_register.add_item("Ritz Crackers", 5.0)
    #     assert(self.cash_register.total == 9.5)
    #     self.cash_register.add_item("Justin's Peanut Butter Cups", 2.50, 2)
    #     assert(self.cash_register.total == 14.5)
    #     self.reset_register_totals()
    

    # def test_items_list_without_multiples(self):
    #     '''returns an array containing all items that have been added'''
    #     new_register = CashRegister()
    #     new_register.add_item("eggs", 1.99)
    #     new_register.add_item("tomato", 1.76)
    #     assert(new_register.items == ["eggs", "tomato"])

    # def test_items_list_with_multiples(self):
    #     '''returns an array containing all items that have been added, including multiples'''
    #     new_register = CashRegister()
    #     new_register.add_item("eggs", 1.99, 2)
    #     new_register.add_item("tomato", 1.76, 3)
    #     assert(new_register.items == ["eggs", "eggs", "tomato", "tomato", "tomato"])

# **Hint #2:** The `apply_discount()` method requires some knowledge about working
# with integers versus floats in Python. When you get to that method, take a look
# at what return value the tests are expecting and keep in mind that Python
# provides methods for changing an Integer to a Float and vice versa.        

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    # def test_apply_discount(self):
    #     '''applies the discount to the total price.'''
    #     self.cash_register_with_discount.add_item("macbook air", 1000)
    #     self.cash_register_with_discount.apply_discount()   
    #     assert(self.cash_register_with_discount.total == 800)
    #     # self.cash_register_with_discount.total = 0
    #     self.reset_register_totals()

    # def test_apply_discount_success_message(self):
    #     '''prints success message with updated total'''
    #     captured_out = io.StringIO()
    #     sys.stdout = captured_out
    #     self.cash_register_with_discount.add_item("macbook air", 1000)
    #     self.cash_register_with_discount.apply_discount()
    #     sys.stdout = sys.__stdout__
    #     assert(captured_out.getvalue() == "After the discount, the total comes to $800.\n")
    #     self.reset_register_totals()

    # def test_apply_discount_reduces_total(self):
    #     '''reduces the total'''
    #     self.cash_register_with_discount.add_item("macbook air", 1000)
    #     self.cash_register_with_discount.apply_discount()
    #     assert(self.cash_register_with_discount.total == 800)
    #     self.reset_register_totals()

    # def test_apply_discount_when_no_discount(self):
    #     '''prints a string error message that there is no discount to apply'''
    #     captured_out = io.StringIO()
    #     sys.stdout = captured_out
    #     self.cash_register.apply_discount()
    #     sys.stdout = sys.__stdout__
    #     assert(captured_out.getvalue() == "There is no discount to apply.\n")
    #     self.reset_register_totals()

# **Hint #3:** The `void_last_transaction()` method will remove the last
# transaction from the total. You'll need to make an additional attribute and keep
# track of that last transaction amount somehow. In what method of the class are
# you working with an individual item?            

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0

    # def test_void_last_transaction(self):
    #   '''subtracts the last item from the total'''
    #   self.cash_register.add_item("apple", 0.99)
    #   self.cash_register.add_item("tomato", 1.76)
    #   self.cash_register.void_last_transaction()
    #   assert(self.cash_register.total == 0.99)
    #   self.reset_register_totals()

    # def test_void_last_transaction_with_multiples(self):
    #   '''returns the total to 0.0 if all items have been removed'''
    #   self.cash_register.add_item("tomato", 1.76, 2)
    #   self.cash_register.void_last_transaction() 
    #   assert(self.cash_register.total == 0.0)
    #   self.reset_register_totals()

# **Hint #4:** Python handles mutable default values for arguments differently
# than it handles immutable default values. This means that you should usually not
# set default values for lists, dictionaries, and instances of classes. You can
# learn more on this quirk in Python's documentation on [More Control Flow Tools
# ](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values).


# lib/testing/cash_register_test.py:8: in <module>
#     class TestCashRegister:
# lib/testing/cash_register_test.py:12: in TestCashRegister
#     cash_register_with_discount = CashRegister(20)
# E   TypeError: CashRegister() takes no arguments


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


        