# SecureCLI: A Command Line Password Manager

#### Video Demo:  <URL HERE>

---

### Description:

**SecureCLI** is a secure and user-friendly command-line password manager designed specifically for Unix-based and Linux-based systems. The tool allows users to generate strong, random passwords, store them securely in an encrypted local database, and retrieve or manage them—all from a simple command-line interface. Built as my final project for CS50P, this program emphasizes both functionality and security, while providing an intuitive experience.

This project was inspired by the need for a lightweight, no-internet-required password manager that developers and privacy-conscious users can operate from the terminal. It employs modern cryptography techniques and password handling practices to ensure that sensitive user data remains private and safe.

---

### Files and Their Roles:


- **project.py**: The main entry point of the application. This script make sure that user is on a unix or linux device and displays a menu to the user with available operations: 
    1. Save a user chosen password,
    2. Generate and list passwords,
    3. Generate and save passwords,
    4. View all saved passwords,
    5. update a password,
    6. Delete a password,
    7. Delete all the password,
    8. exit the proggream.

- **genrate.py**: Contains the core logic for generating random passwords. The function utilizes uppercase letters, lowercase letters, numbers, and symbols to create strong passwords of a user-defined length.

- **save.py**: Implements functionality for saving a user-supplied password into the encrypted local database. Inputs include website/label, username, password, and the Date on which passowrd is saved. It uses the `cryptography.fernet` module for encryption and `sqlite3` for database handling.

- **save_random**: Generates random passwords, lists them to the user, prompts the user to choose any one, encrypts, and saves the user-chosen password.

- **print_pass.py**: Responsible for fetching and decrypting saved passwords and displaying them to the user in a readable format.

- **update.py**: Contains features for updating or deleting entries from the password database securely.

- **setup.py**: Initializes the project on first run. It generates an encryption key, creates a `.user` file with the user's name, and sets up the SQLite database with the required table structure.

- **test_project.py**: Contains unit tests for major functions. Using Python’s `unittest.mock`, it tests password generation, data saving, and welcome display. These tests ensure the app works as expected without depending on user input or external factors.

- **.key**: A securely generated symmetric key stored locally for encrypting and decrypting passwords.

- **.pass.db**: The local SQLite database file that stores all saved password entries securely.

- **.user**: Contains the username that is displayed with a stylized welcome banner.

---

### Design Choices:

One of the key decisions was to prioritize **local encryption** using `cryptography.Fernet`. This ensures that even if the `.pass.db` file is accessed by an attacker, they cannot read any of the saved passwords without the `.key` file.

Another important design choice was using **modular Python files**. Each function (generate, save, print, update) was split into different files to follow separation of concerns and improve code readability and maintainability.

The CLI-based interface makes it fast and accessible for developers and power users. It avoids the complexity of a GUI while still being clear and functional.

---

This project helped me understand and apply concepts like file handling, encryption, database management, testing, and modular programming in a real-world context. I'm proud of building something that’s both useful and educational.

> **Note**: Please ensure you have Python 3.10+ installed,  run: pip install -r requirements.txt, and run setup.py before starting the program to initialize all required files.

---

Thanks for reading.


