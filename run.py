#!/usr/bin/env python3.9
import random #to import random password generator
from users import User
from credentials import User_Credentials


def create_credential(acc_name, acc_password):
    '''
    Function to create a new credential
    '''
    new_credential = User_Credentials(acc_name, acc_password)
    return new_credential


def save_credential(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()


def del_credentials(credentials):
    '''
    Function to delete a credential
    '''
    credentials.delete_credentials()


def find_credential(acc_name):
    '''
    Function that finds a credential and returns it
    '''
    return User_Credentials.find_by_name(acc_name)


def check_existing_credentials(name):
    '''
    Function that check if a credential exists with that name and return a Boolean
    '''
    return User_Credentials.find_by_name(name)


def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return User_Credentials.display_credentials()

def main():
    while True:
        print("Welcome to password Locker.")
        print("This app will keep you from the bassle and hassle of remembering your passwords for good.")
        print("Use these short codes to select an option:") 
        print("-"*50)
        print("To create a new user account, type: 'nu'")
        print("To sign in to your account, type: 'si'")
        print("To exit password locker, type: 'end'")
        print("-"*50)
        
        short_code = input().lower()
        print('\n')

        if short_code == 'nu':
            print("Create your choice of username")
            print("-"*40)
            new_username = input()

            print("Create your choice of password")
            print("-"*25)
            new_password = input()

            print("Confirm your inputted password")
            print("-"*16)
            confirm_password = input()

            while confirm_password != new_password:
                print("Sorry, the passwords inserted did not match! Please try again.")
                print("Enter a new password")
                new_password = input()
                print("Confirm Your Password")
                confirm_password = input()
            else:
                print(f"Great to have you {new_username} join pur service! You new account has been created and activated.")
                print("-"*50)
                print('\n')
                print("Do you wish to proceed to your Account?")
                print("-"*30)
                print("Enter your Username:")
                created_username = input()
                print("Enter your Password:")
                created_password = input()

                while created_username != new_username or created_password != new_password:
                    print("You entered a wrong username or password please retry!")
                    print("Username:")
                    created_username = input()
                    print("Your Password")
                    created_password = input()
                    print("-"*24)
                else:
                    print(f"Greetings {created_username}, welcome to your Account")
                    print("Select an option below to continue: Enter either a, b, c, d or e to continue.")
                    print("-"*57)
                    print('\n')

                while True:
                    print("a: View saved account")
                    print("b: Add new account")
                    print("c: Remove existing account")
                    print("d: Search for existing account")
                    print("e: Log Out")
                    print("-"*57)
                    print('\n')
                    option = input()
                    print("-"*50)

                    if option == 'b':
                        while True:
                            print("Continue to add? Type y(for yes)/n(for no)")

                            choice = input().lower()
                            if choice == 'y':
                                print("Enter The Account Name")
                                print("-"*35)
                                acc_name = input()
                                print("Enter a password")
                                print("-"*35)
                                print('\n')
                                print("To generate random password enter keyword 'gen' or 'n' to create your own password")
                                keyword = input().lower()
                                if keyword == 'gen':
                                    acc_password = random.randint(111111, 1111111)
                                    print(f"Account: {acc_name}")
                                    print(f"Password: {acc_password}")
                                    print('\n')

                                elif keyword == 'n':
                                    print("Create your password")
                                    acc_password = input()
                                    print(f"Account: {acc_name}")
                                    print(f"Password: {acc_password}")
                                    print('\n')

                                else:
                                    print("Please enter a valid Code")

                                save_credential(create_credential(
                                    acc_name, acc_password))
                            elif choice == 'n':
                                break
                            else:
                                print("Please use 'y' for yes or 'n' for no!")
                    elif option == 'a':
                        while True:
                            print("Your registered accounts are as listed below:")
                            print("-"*40)
                            if display_credentials():

                                for credential in display_credentials():
                                    print(f"ACCOUNT NAME:{credential.acc_name}")
                                    print(f"PASSWORD:{credential.acc_password}")

                            else:
                                print('\n')
                                print("It appears you do not have any accounts yet")
                                print('\n')

                            print("Return to Main Menu? Type y(for yes)/n(for no)")

                            back = input().lower()
                            if back == 'y':
                                break
                            elif back == 'n':
                                continue
                            else:
                                print("Please Enter a valid code")
                                continue

                    elif option == 'e':
                        print("You will log out of your account. Type y(for yes)/n(for no) to continue...")
                        logout = input().lower()

                        if logout == 'y':
                            print("You have Successfully logged out of your account. Goodbye")
                            break
                        elif logout == 'n':
                            continue
                    elif option == 'c':
                        while True:
                            print("Search for account to delete")

                            search_name = input()

                            if check_existing_credentials(search_name):
                                search_credential = find_credential(search_name)
                                print(f"ACCOUNT NAME: {search_credential.acc_name} \n PASSWORD: {search_credential.acc_password}")
                                print("Delete? y(for yes)/n(for no)")
                                proceed = input().lower()
                                if proceed == 'y':
                                    del_credentials(search_credential)
                                    print("Account deleted")
                                    break
                                elif proceed == 'n':
                                    continue

                            else:
                                print("Contact Does not exist")
                                break

                    elif option == 'd':
                        while True:
                            print("Continue? type y(For yes)/n(For no)")
                            optionb = input().lower()
                            if optionb == 'y':
                                print("Enter an account name")
                                print("-"*20)

                                search_name = input()

                                if check_existing_credentials(search_name):
                                    search_credential = find_credential(
                                        search_name)
                                    print(f"ACCOUNT NAME: {search_credential.acc_name} . PASSWORD: {search_credential.acc_password}")
                                    print("-"*20)
                                else:
                                    print("That Account Does not exist")
                            elif optionb == 'n':
                                break
                            else:
                                print("Please enter a valid code")

                    else:
                        print("Please enter a valid code")
                        continue

        elif short_code == 'si':
            print("Welcome")
            print("Enter username")
            default_user_name = input()

            print("Enter password")
            default_user_password = input()
            print('\n')

            while default_user_name != 'example' or default_user_password != '12@34':
                print("Wrong username/Password. Default Username is 'example' and password is '12@34'")
                print("Enter Username")
                default_user_name = input()

                print("Enter Your password")
                default_user_password = input()

                print('\n')

            if default_user_name == 'example' and default_user_password == '12@34':
                print("Login Successful!")
                print('\n')
                print("Select an option below to continue: Enter 1, 2, 3, 4 or 5")
                print('\n')

            while True:
                print("1: View saved account")
                print("2: Add new account")
                print("3: Remove account")
                print("4: Search account")
                print("5: Log Out of account")

                option = input()

                if option == '2':
                    while True:
                        print("Continue to add? Type y (for yes)/n (for no)")

                        choice = input().lower()

                        if choice == 'y':
                            print("Enter Account Name")
                            acc_name = input()
                            print("Enter a password")
                            print("To generate random password enter keyword 'gp' or 'n' to create your own password")
                            keyword = input().lower()
                            if keyword == 'gp':
                                acc_password = random.randint(111111, 1111111)
                                print(f"Account: {acc_name}")
                                print(f"Password: {acc_password}")
                                print('\n')
                            elif keyword == 'n':
                                print("Create your password")
                                acc_password = input()
                                print(f"Account: {acc_name}")
                                print(f"Password: {acc_password}")
                                print('\n')

                            else:
                                print("Please enter a valid Code")

                            save_credential(create_credential(acc_name, acc_password))
                        elif choice == 'n':
                            break
                        else:
                            print("Please use 'y' for yes or 'n' for no!")
                elif option == '1':
                    while True:
                        print("Listed below are all your accounts")
                        if display_credentials():

                            for credential in display_credentials():
                                print(f"ACCOUNT NAME:{credential.acc_name}")
                                print(f"PASSWORD:{credential.acc_password}")

                        else:
                            print('\n')
                            print("You don't seem to have any contacts yet")
                            print('\n')

                        print("Back to Main Menu? y(For yes)/n(For no)")

                        back = input().lower()
                        if back == 'y':
                            break
                        elif back == 'n':
                            continue
                        else:
                            print("Please Enter a valid code")
                elif option == '5':
                    print("You will be logged out of your account. Are you sure? y/n")
                    logout = input().lower()

                    if logout == 'y':
                        print("You have Successfully logged out")
                        break
                    elif logout == 'n':
                        continue

                elif option == '3':
                    while True:
                        print("Search for credential to delete")

                        search_name = input()

                        if check_existing_credentials(search_name):
                            search_credential = find_credential(search_name)
                            print(f"ACCOUNT NAME: {search_credential.acc_name} \n PASSWORD: {search_credential.acc_password}")
                            print("Delete? y/n")
                            sure = input().lower()
                            if sure == 'y':
                                del_credentials(search_credential)
                                print("Account deleted")
                                break
                            elif sure == 'n':
                                continue

                        else:
                            print("That account Does not exist")
                            break

                elif option == '4':
                    while True:
                        print("Continue? y/n")
                        option2 = input().lower()
                        if option2 == 'y':
                            print("Enter an account name")

                            search_name = input()

                            if check_existing_credentials(search_name):
                                search_credential = find_credential(
                                    search_name)
                                print(f"ACCOUNT NAME: {search_credential.acc_name} \n PASSWORD: {search_credential.acc_password}")
                            else:
                                print("That Contact Does not exist")
                        elif option2 == 'n':
                            break
                        else:
                            print("Please enter a valid code")
                else:
                    print("Please enter a valid code")
        elif short_code == 'end':
            break
        else:
            print("Please Enter a valid code to continue")


if __name__ == '__main__':
    main()








