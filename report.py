from PyInquirer import prompt
import csv


def get_status():
    # Initialize lists to store users and expenses
    users = []
    expenses = []
    # Initialize a list to store the parsed data
    parsed_data = []

    # Read the CSV file
    with open('expense_report.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        
        for row in csv_reader:
            # Check if the row has at least 4 columns before accessing the fourth column
            if len(row) >= 4:
                amount = row[0]
                users = [user.strip() for user in row[3].strip('[]').split(',')]
                
                # Create a dictionary to represent each row
                row_data = {
                    'amount': amount,
                    'spender': row[1],
                    'users': users
                }
                
                # Append the dictionary to the parsed_data list
                parsed_data.append(row_data)

    user_balances = {}  # Dictionary to store user balances

    for user in users:
        user_balances[user.name] = 0  # Initialize balances to zero

    for expense in expenses:
        split_amount = expense.amount / len(expense.users)  # Equal split among users
        for user in expense.users:
            user_balances[user] += split_amount

    
    # Now, parsed_data contains a list of dictionaries with 'amount' and 'users' keys for each row in the CSV file
    print(parsed_data)