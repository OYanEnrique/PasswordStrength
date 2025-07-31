# PasswordStrength
A simple Python script that simulates an account creation and login system. It checks password strength, requires a strong password, and then validates user credentials.

# 🔐 Simple Account & Login Simulator

This is a command-line Python script that simulates a basic user account creation and login process. The program guides the user through creating a username and a secure password, and then prompts them to log in with their newly created credentials.

## Features

1.  **Password Strength Checker:**
    * The program first evaluates the strength of the user's chosen password based on its length.
    * It provides feedback, classifying the password as "Weak," "Ok," or "Strong."

2.  **Secure Password Enforcement:**
    * If the initial password is not "Strong" (i.e., less than 13 characters), the program enters a loop, forcing the user to create a new password until it meets the length requirement for a strong password.

3.  **Login Simulation:**
    * After a valid account is created, the program simulates a login screen.
    * It prompts the user for their username and password.
    * A `while` loop validates the credentials, showing an error message and re-prompting if the details are incorrect.
    * Once the correct username and password are provided, a "Logged in!" message is displayed.

## How to Use

1.  Make sure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `PasswordStrength.py`).
3.  Open your terminal or command prompt.
4.  Run the script with the following command:
    ```sh
    python PasswordStrength.py
    ```
5.  Follow the on-screen instructions to create your username, set a strong password, and then log in.
