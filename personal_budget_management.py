# Task #1: Define Budget Category Class 
# A 'BudgetCategory' class capable of storing category details securely.

# Task #2: Implement Getters and Setters 
# Methods that allow controlled access and modification of the private attributes, with validation checks in place.

# Task #3: Add Budget Functionality 
# Ability to track expenses per category and update the remaining budget safely.

# Task #4: Display Budget Details 
# Users can view a summary of each budget category, showcasing encapsulation in action.

class BudgetCategory:
    '''The BudgetCategory class takes a category name and an allocated budget. Budget expenses are set to 0.'''
    def __init__(self, category_name, allocated_budget, expense = 0):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__expense = expense
    
    def get_category_name(self):
        '''Retrieves category name.'''
        return self.__category_name
    
    def get_allocated_budget(self):
        '''Retrieves allocated budget.'''
        return self.__allocated_budget
    
    def get_remaining_budget(self):
        '''Retrieves remaining budget from the allocated budget minus the expenses.'''
        return (self.__allocated_budget - self.__expense)
    
    def set_budget(self, amount):
        '''Updates the allocated budget to the given amount.'''
        try: 
            # If the amount is not a float or int or if self is not a BudgetCategory object, it will raise an error.
            if (not isinstance(self, BudgetCategory)) and (not isinstance(amount, float)) and (not isinstance(amount, int)):
                raise TypeError()
            elif amount > 0:
                # The amount must be positive.
                self.__allocated_budget = amount
                return True
            else:
                raise ValueError()
        except TypeError:
            print("Please input a valid number.")
            return False
        except ValueError:
            print("The budget must be greater than 0.")
            return False
            
    def add_expense(self, amount):
        # Method to add an expense to the category
        try: 
            # If the amount is not a float or int or the self is not a BudgetCategory, raise error.
            if (not isinstance(self, BudgetCategory)) and (not isinstance(amount, float)) and (not isinstance(amount, int)):
                raise TypeError()
            # The amount cannot exceed the remaining budget
            if self.get_remaining_budget() - amount >=0:
                self.__expense += amount
                return True
            else: 
                raise ValueError()
        except TypeError:
            print("Error occurred: Type Error.")
            return False
        except ValueError:
            print("The amount exceeds the budget.")
            return False
            
    def display_category_summary(self):
        # Method to display the budget category details
        print(f"Category: {self.get_category_name()}, Allocated Budget: ${self.get_allocated_budget():.2f}, Remaining Budget: ${self.get_remaining_budget():.2f}")

print("\nTest #1: Basic trial - Does it work? (Food, Allocated Budget = $800, Expense = $100)'")
food = BudgetCategory("Food", 800)
food.add_expense(100)
food.display_category_summary()

print("\nTest #2: If we adjust the budget, the remaining budget should automatically adjust. (Adjust Budget = $700)")
food.set_budget(700)
food.display_category_summary()

print("\nTest #3: Will it take a float? (Expense = $50.25)")
food.add_expense(50.25)
food.display_category_summary()

print("\nTest #4: It shouldn't take a string. (Expense = 'hello')")
entertainment = BudgetCategory("Entertainment", 100)
entertainment.display_category_summary()
entertainment.add_expense("hello")

print("\nTest #5: What if we overspend? (Expense = $200)")
entertainment.add_expense(200)
entertainment.display_category_summary()

print("\nTest #6: What if we spend all our budget? (Expense = $100)")
entertainment.add_expense(100)
entertainment.display_category_summary()

print("\nTest #7: Let's create a list of budget categories, display them all and create a little app.")
bills = BudgetCategory("Bills", 1500)
rent = BudgetCategory("Rent", 1000)
health_care = BudgetCategory("Health Care", 200)
transportation = BudgetCategory("Transportation", 100)
budget = {food.get_category_name():food, entertainment.get_category_name(): entertainment, bills.get_category_name():bills, rent.get_category_name():rent, health_care.get_category_name():health_care, transportation.get_category_name():transportation}

for category in budget.keys(): 
    budget[category].display_category_summary()

while True: 
    try: 
        # Main menu
        action = input("\nMenu: \n1. Add Expense \n2. Set Budget \n3. Display All Budget Categories \n4. Add New Budget Category \n5. Quit\n\nEnter an action (1-5): ")

        # 5 = Quit
        if action == "5":
            print("\nPersonal Budget Management Closed.")
            break
        # 1 = Add Expense
        elif action == "1": 
            # Prompt budget category
            budget_category = input("\nEnter budget category: ")
            found = False
            for name in budget:
                # Find the budget category
                if budget_category.lower() == name.lower():
                    # Prompt expense
                    expense = float(input("\nEnter expense: "))
                    # Add expense
                    if budget[name].add_expense(expense):
                        print(f"\nA new expense {expense:.2f} has been added to the budget category '{budget_category}'.")
                    # Display new budget category summary
                    budget[name].display_category_summary()  
                    found = True
            # Alert user if not found
            if found == False: 
                print(f"Budget category '{budget_category}' not found.")
        # 2 = Set Budget
        elif action == "2":
            # Prompt budget category
            budget_category = input("Enter budget category: ")
            found = False
            for name in budget:
                # Find budget category
                if budget_category.lower() == name.lower():
                    # Remind user what the current budget is
                    print(f"\nThe current allocated budget is: {budget[budget_category].get_allocated_budget():.2f}")
                    # Prompt new allocated budget
                    allocated_budget = float(input("Enter new allocated budget: "))
                    # Set budget with new allocated budget
                    if budget[budget_category].set_budget(allocated_budget):
                        print(f"\nThe allocated budget for '{budget_category}' has been updated.")
                    # Display updated budget category summary
                    budget[budget_category].display_category_summary()
                    found = True
            # Alert user if budget category not found
            if found == False:
                print(f"\nBudget category '{budget_category}' not found.")
        # 3 = Display Budget Categories
        elif action == "3":
            # Iterate over each category and display
            for name, category in budget.items(): 
                category.display_category_summary()
        # 4 = Add New Budget Category
        elif action == "4":
            # Prompt new budget category
            budget_category = input("\nEnter new budget category: ")
            # Prompt allocated budget
            allocated_budget = float(input("\nEnter allocated budget: "))
            # Create budget category and add it to the list
            budget[budget_category] = BudgetCategory(budget_category, allocated_budget)
            print(f"\nThe new budget category '{budget_category}' has been added with the allocated budget ${allocated_budget:.2f}")
        else:
            raise ValueError()
    except ValueError:
        print("Invalid input.")
    except Exception as e:
        print(f"An error occurred: {e}")
