import calendar
import datetime
import sys
import json 
from expense import Expense
from user import *

class BudgetTracker:

    def __init__(self):
        self._user_dico = {}
        self._user = User()
        self._expense_file = "expenses.csv"

        self._categories = {'1':'Food|Groceries', '2':'Mortgage|Rent', '3':'Utilities', 
                            '4':'Pets', '5':'Leisure', '6':'Misc.'}

        with open("users.json", 'r') as user_infile:
            user_info = json.load(user_infile)
            self._user_dico = user_info

        for person in self._user_dico:
            self._username =  person
            self._budget = self._user_dico[person]["Budget"]
            self._currency = self._user_dico[person]["Currency"]

    def get_user_expense(self):
        user_category = False

        self.expense_description = input("Enter expense description (e.g. name): ")
        self.expense_amount = float(input("Enter amount: "))

        print("\nSelect a category: \n")

        while user_category is False:
            for key, category_name in self._categories.items():
                print(f"{key}. {category_name}")

            category_choice = ((input("\nChoice: ")))

            if category_choice in self._categories: 
                selected_choice = self._categories[category_choice]
                user_category = True
                return Expense(description=self.expense_description, category=selected_choice, amount=self.expense_amount)
            
            else:
                print("Invalid option. Choose again. ")

        user_category = False

    def save_expense_csv(self, expense:Expense, expense_file):
        with open(expense_file, 'a') as expense_outfile:
            expense_outfile.write(f"{expense._category},{expense._description},{expense._amount}\n")


    def summarize_expenses(self, expense_file, user_budget):
        self.expenses: list[Expense] = []

        with open(expense_file, 'r') as expense_infile:
            lines = expense_infile.readlines()

            for line in lines:
                expense_description, expense_category, expense_amount  = line.strip().split(",")

                line_expense = Expense(
                    category=expense_category,
                    description=expense_description,
                    amount = float(expense_amount))

                self.expenses.append(line_expense)

        self.amount_by_category = {}
        
        for expense in self.expenses:
            key = expense._category

            if key in self.amount_by_category:
                self.amount_by_category[key] += expense._amount
            else:
                self.amount_by_category[key] = expense._amount
        
        print(f"\n{self._username}'s Expenses by Category \n")

        for key, amount in self.amount_by_category.items():
            print(f" {key}: {self._currency}{amount:.2f}")
        
        self.total_spent = sum([x._amount for x in self.expenses])
        print(f"\nTotal spent: {self._currency}{self.total_spent:.2f}")

        self.remaining_budget = float(self._budget) - self.total_spent
        print(f"Budget remaning: {self._currency}{self.remaining_budget:.2f}")

        self.now = datetime.datetime.now()
        self.days_in_month = calendar.monthrange(self.now.year, self.now.month)[1]
        self.remaining_days = self.days_in_month - self.now.day

    def daily_budget(self):

        daily_remain = self.remaining_budget / self.remaining_days

        if self.remaining_budget >= 0:
            print(f"\033[92mBudget per day: {self._currency}{daily_remain:.2f}\033[0m")
        else:
            abs(daily_remain)
            print(f"\033[91mBudget per day: {self._currency}{daily_remain:.2f}\033[0m")

    def enter_another_expense(self):

        another = input("Enter another expense (y or n)?: ")

        match another:
            case "y":
               self.run_budget_tracker()
            case "n":
                sys.exit("Goodbye")
            case _:
                print(f'Not a valid answer. Choose y or n.')
                self.enter_another_expense()

    def run_budget_tracker(self):

        expense = self.get_user_expense()
        file = self._expense_file
        budget = self._budget

        self.save_expense_csv(expense, file)
        self.summarize_expenses(file, budget) 
        self.daily_budget()
        self.enter_another_expense()


def main():
    print("Welcome to BudgetTrackr2.0\n")
    bt = BudgetTracker()
    bt.run_budget_tracker()


if __name__== "__main__":
    main()
