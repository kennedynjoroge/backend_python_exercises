"""Objective: Code to host logic for simple ATM menu display, validation and backoffice operations.
Implementation Approach: Uses functions to modularize the code for simplicity, maintainability and reuse.using
"""

# Import libraries
from random import randrange

# Variables
user_accounts = {}
user_balances = {}
user_service_requests = {}


def display_landing_menu():
    print("Welcome to CommAfrica Bank Virtual ATM\n")
    print("Select one of below available options")
    try:
        selected_action = int(float(input("1: Register for New Account \n2: Login \n3: Help \n")))
        return selected_action
    except Exception as e:
        print(e)
        print("Invalid input. Please retry")
        display_landing_menu()


def generate_user_pin():
    return randrange(1000, 9999)


def generate_account_number():
    return randrange(1000, 9990)
    # return (randrange(1000000, 9999999))


def register_new_account():
    """To capture user supplied details for new account registration"""

    print("Please input your personal details below\n")
    first_name = input("First name: ")
    last_name = input("\nLast name: ")
    try:
        id_number = int(input("\nID number: "))
    except Exception as e:
        print(e)
        print("Input error. Please input a number")
        id_number = int(input("\nID number: "))

    email_address = input("\nEmail Address: ")

    # Generate account number and pin
    new_pin = generate_user_pin()
    account_number = generate_account_number()

    user_accounts[account_number] = [first_name, last_name, id_number, email_address, new_pin]
    print(f"Thank you for registration. Your account number is {account_number}. New pin is {new_pin}")
    print("\n Keep your account and pin details safe.")


def customer_login():
    print("=====Customer Login======\n")
    print("Please input your account details \n")
    try:
        account_input = int(input("Account number: "))
        password_input = int(input("\nPassword: "))
        for account_number, user_details in user_accounts.items():
            if (account_number == account_input) and (user_details[4] == password_input):
                bank_operations_menu(account_number, user_details)
            else:
                print("Invalid account or password. Please retry")
                customer_login()
    except Exception as e:
        print(e)
        print("Invalid account or password. Please retry")
        customer_login()


def customer_help():
    print("====HELP MENU===")
    print("Option 1 is to register for a new account if you do not have an account with us.\n")
    print("Option 2 is to requires login with your account number and pin.\n")
    main()


def bank_operations_menu(account_number, user_details):
    '''Post login operations display and selection'''
    print(f"Welcome {user_details[0]} to bank operations")
    print("Select one of below available options")
    try:
        operation_option = int(float(input("1: Withdraw \n2: Deposit \n3: Account Balance \n4: Service Request \n5: "
                                           "Exit\n")))
        if operation_option == 1:  # Withdraw
            withdrawal_operation(account_number)
        elif operation_option == 2:  # Deposit
            deposit_operation(account_number)
        elif operation_option == 3:  # Account Balance
            account_balance = get_account_balance(account_number)
            print(f"Your balance is {account_balance}")
            bank_operations_menu(account_number, user_details)
        elif operation_option == 4:  # Service Request
            service_request(account_number)
        elif operation_option == 5:  # Exit
            logout(account_number)
        else:
            print("Invalid input Please retry.")
            bank_operations_menu(account_number, user_details)
    except Exception as e:
        print(e)
        print("Invalid input. Please retry.")
        bank_operations_menu(account_number, user_details)


def get_account_balance(account_number):
    account_balance = user_balances[account_number] = 0
    return account_balance


def withdrawal_operation(account_number):
    try:
        account_balance = get_account_balance(account_number)
        withdraw_amt = float(input("How much would you like to withdraw? \n"))
        user_balances[account_number] = account_balance - withdraw_amt
        print(f"Your balance is {user_balances[account_number]}. Take your cash")
    except Exception as e:
        print(e)
        print("Error encountered. Please retry")
        main()


def deposit_operation(account_number):
    try:
        account_balance = get_account_balance(account_number)
        deposit_amt = float(input("How much would you like to deposit? \n"))
        user_balances[account_number] = account_balance + deposit_amt
        print(f"Your new balance is {user_balances[account_number]}. Thank you")
    except Exception as e:
        print(e)
        print("Error encountered. Please retry")
        main()


def service_request(account_number):
    cus_service_request = input("What issue would you like to report? \n")
    user_service_requests[account_number] = cus_service_request
    print("Thank you for contacting us")
    main()


def logout(account_number):
    main()


def main():
    """Main entry procedure of the ATM"""
    selected_action = display_landing_menu()
    if selected_action == 1:  # registration
        register_new_account()
        customer_login()
    elif selected_action == 2:  # login
        customer_login()
    elif selected_action == 3:  # help
        customer_help()
    else:
        print("You have selected an invalid option")
        main()


# Start Program
if __name__ == "__main__":
    main()
