#!/usr/bin/env python3

"""
Define a simple console password generator
based on user input.
"""

import csv
import string
import secrets


def generate_password(length):
    """
    Generate a random password of the specified length.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password


def save_credentials(account, username, email, password):
    """
    Save the account, username, email and password in a CSV file.
    """
    with open("credentials.csv", "a", newline="") as csvfile:
        fieldnames = ["Account", "Username", "Email", "Password"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow(
            {
                "Account": account,
                "Username": username,
                "Email": email,
                "Password": password,
            }
        )


def main():
    print("Welcome to the Simple Console Password Generator!")
    print()

    while True:
        account = input("Enter account (type 'quit' to exit): ")

        if account.lower() == "quit":
            print("Exiting the program. Goodbye!")
            break

        username = input("Enter username: ")
        email = input("Enter email: ")

        while True:
            try:
                length = int(input("Enter password length (must be >= 8: "))
                if length < 8:
                    print("Length must be greater or equal to 8.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        password = generate_password(length)
        print()
        print(f"Generated password ==>: {password}")

        save_option = input("Do you want to save these credentials? (yes/no): ").lower()
        if save_option == "yes":
            save_credentials(account, username, email, password)
            print("Credentials saved successfully.")
        else:
            print("Credentials not saved.")
        print()


if __name__ == "__main__":
    main()
