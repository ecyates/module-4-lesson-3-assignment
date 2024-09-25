# Module 4 - Lesson 3 - OOP Principles
Author: Elizabeth Yates

In this repository, I completed the following assignment: 

## 1. Encapsulation in Personal Budget Management (personal_budget_management.py)

Objective: The aim of this assignment is to reinforce the understanding of encapsulation in Python, focusing on the use of private attributes and getters and setters.

Problem Statement: You are required to build a Personal Budget Management application. The application will manage budget categories like food, entertainment, utilities, etc., ensuring that budget details remain private and are accessed or modified through public methods.

### Task 1: Define Budget Category Class 

- Create a class `BudgetCategory` with private attributes for category name and allocated budget. 
- Initialize these attributes in the constructor.

Expected Outcome: A `BudgetCategory` class capable of storing category details securely.

### Task 2: Implement Getters and Setters 

- Write getter and setter methods for both the category name and the allocated budget. 
- Ensure that the setter methods include validation (e.g., budget should be a positive number).

Expected Outcome: Methods that allow controlled access and modification of the private attributes, with validation checks in place.

### Task 3: Add Budget Functionality 

- Implement a method to add expenses to a category and adjust the budget accordingly. 
- Validate the expense amount before making deductions from the budget.

Expected Outcome: Ability to track expenses per category and update the remaining budget safely.

### Task 4: Display Budget Details 

- Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses.

Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action.

### Code Examples:

    class BudgetCategory:
        # Constructor and private attributes
        # ...

        # Getters and setters for category name and budget
        # ...

        def add_expense(self, amount):
            # Method to add an expense to the category
            # ...

        def display_category_summary(self):
            # Method to display the budget category details
            # ...

    food_category = BudgetCategory("Food", 500)
    food_category.add_expense(100)
    food_category.display_category_summary()