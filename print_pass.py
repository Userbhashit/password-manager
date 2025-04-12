import sqlite3
import pyperclip
from getpass import getpass
from tabulate import tabulate
from cryptography.fernet import Fernet

def main():

    # Load the key
    with open(".key", "rb") as key_file:
        key = key_file.read()

    f = Fernet(key)

    # Load encrypted stored password
    with open(".pass", "rb") as p:
        encrypted_pass = p.read()

    # Decrypt the stored password once
    decrypted_pass = f.decrypt(encrypted_pass)

    # User authentication loop
    while True:
        user_pass = getpass("Please provide the password (or enter '.' to exit): ")

        if user_pass == ".":
            return

        if user_pass.encode() == decrypted_pass:
            break
        else:
            print("Incorrect password. Please try again.")


    db = sqlite3.connect(".pass.db")  # type: ignore
    pointer = db.cursor()
    passwords = pointer.execute("SELECT * FROM passwords").fetchall()

    decrypted_rows = []
    for row in passwords:
        id, label, username, encrypted_password, date = row
        # If encrypted_password is TEXT in DB, decode it to bytes
        if isinstance(encrypted_password, str):
            encrypted_password = encrypted_password.encode()
        password = f.decrypt(encrypted_password).decode()
        decrypted_rows.append((id, label, username, password, date))

    print(tabulate(decrypted_rows, headers=["ID", "Website/Label", "UserName", "Password", "Created on"], tablefmt="pretty"))
    
    while True:
        try:
            id = int(input("Enter the Id number you want to copy(or 0 to exit): "))
            break
        except ValueError:
            print("Not a number.")
            continue

    if id == 0:
        return
    else:
        while True:
            try:
                pass_to_copy = pointer.execute("SELECT password FROM passwords WHERE id=?", (id,)).fetchone()
                pass_to_copy = f.decrypt(pass_to_copy[0]).decode()
                pyperclip.copy(pass_to_copy)
                print("Copied to clipboard.")
                break
            except:
                print("Please enter a valid ID.")
    db.close()

if __name__ == "__main__":
    main()
