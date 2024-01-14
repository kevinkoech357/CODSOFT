# Simple Console Password Generator

This Python script is a simple console password generator based on user input. It allows users to input account details, such as account name, username, email, and password length, and generates a random password for them. The generated credentials can be saved to a CSV file for future reference.

## Features

- Generate random passwords with customizable length.
- Input account details including account name, username, email.
- Save generated credentials to a CSV file.
- Graceful exit by typing 'quit'.

## Usage

1. Make sure you have Python 3 installed on your system.

2. Clone the repository:

    ```bash
    git clone https://github.com/kevinkoech357/CODSOFT.git
    ```

3. Navigate to the project directory:

    ```bash
    cd CODSOFT/password-generator
    ```

4. Run the script:

    ```bash
    python3 password_generator.py
    ```

5. Follow the on-screen instructions to input account details and generate passwords.

6. Optionally, choose to save the generated credentials to a CSV file.

7. To exit the program, type 'quit' when prompted to enter the account name.

## CSV File

The generated credentials are saved in a CSV file named `credentials.csv` in the project directory. The CSV file has the following columns:

- Account
- Username
- Email
- Password

---

**Note:** This is a simple console application intended for educational purposes. Use generated passwords responsibly and consider security best practices for storing and managing passwords.
