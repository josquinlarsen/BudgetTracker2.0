import json
class User:

    def __init__(self, username = None, password = None, email = None, budget = 0, currency = None):
        self._user_dico = {} 
        self._username = username
        self._password = password
        self._email = email
        self._budget = budget
        self._currency = currency

    def get_user_dico(self):
        return self._user_dico
    
    def get_username(self):
        return self._username

    def set_username(self):
        user_name = input("Please enter a username: ")
        if user_name in self._user_dico:
            print("I'm sorry that name is already taken. Choose again.")
            self.set_username()
        self._username = user_name

    def set_password(self):
        pwd = input("Please enter a password: ")
        self._password = pwd

    def get_password(self):
        return self._password

    def set_email(self):
        user_input = input("Please enter your email: ")
        self._email = user_input 

    def set_budget(self):
        user_input = int(input("Please enter your monthly budget: "))
        self._budget = float(user_input)

    def get_budget(self):
        return self._budget

    def set_currency(self):
        currency_dico = {'USD':'$', 'EUR':'€', 'GBP':'£'}
        user_input = input("Please select your currency (USD, EUR, or GBP): ")
        currency = user_input.upper()
        if currency in currency_dico:
            self._currency = currency_dico[currency]
        else:
            print("That is not an option. \n")
            self.set_currency()
   
    def get_currency(self):
        return self._currency
    
    def add_to_dico(self):
        temp_dico = {}
        temp_dico["Password"] = self._password
        temp_dico["Email"] = self._email
        temp_dico["Budget"] = self._budget
        temp_dico["Currency"] = self._currency
        self._user_dico[self._username] = temp_dico

    def save_as_json(self):
        with open("users.json", "w") as outfile:
            json.dump(self._user_dico, outfile)

    def register_user(self):
        self.set_username()
        self.set_password()
        self.set_email()
        self.set_budget()
        self.set_currency()
        self.add_to_dico()
        self.save_as_json()
    


def main():
    test = User()
    test.register_user()

if __name__ == '__main__':
    main()
