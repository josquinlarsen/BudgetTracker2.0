#BudgetTracker2.0
New version of BudgetTracker - a basic budget tracking program. Written in Python

BudgetTracker2.0 is a cleaned up version of a previous BudgetTracker program. 

This program allows for the creation of a user: initializes a username, password, 
email, monthly budget, and currency(currently, USD, EUR, or GBP). User information 
is saved to a JSON file. Taking the user information stored in the JSON file, 
BudgetTracker allows the user to input expenses, select the expense category, and give 
the expense a description. This data is saved in a CSV file. 

Using the CSV file, BudgetTracker then provides an itemized budget where expenses are 
deducted from the monthly budget. The total and daily amounts and the remaining balance 
are displayed in green (for positive amounts) and red (for negative). 
