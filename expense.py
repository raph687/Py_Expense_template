from PyInquirer import prompt
import csv

def get_Users():
    with open('users.csv', newline='') as csvfile:
        f = open('users.csv', 'r')
        
        lines = f.readlines()

        users = []

        for line in lines:
            users.append(line.strip())
        
        return users

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
]




class Expense:
    '''class expense'''
    def __init__(self, amount, spender, label, users):
        self.amount = amount
        self.label = label
        self.spender = spender
        self.users = users


def new_expense(*args):
    expense_data = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯

    # Create a new Expense object
    expense = Expense(
        expense_data['amount'],
        expense_data['label'],
        "Default",
        []
    )

    spender_option = {
        "type":"list",
        "name":"spender_options",
        "message":"New Expense - Spender:",
        "choices": get_Users()
    }

    expense.amount = expense_data['amount']
    expense.label = expense_data['label']

    spender = prompt(spender_option)['spender_options']

    expense.spender = spender
    expense.users = get_Users()
    
    f = open('expense_report.csv', 'a', newline='')
    f.write(expense.amount + ";" + expense.spender + ";" + expense.label + "; [" + ", ".join(expense.users) + "]\n")
    
    print("Expense Added !")
    return True


