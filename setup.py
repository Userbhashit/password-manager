from cryptography.fernet import Fernet
from getpass import getpass 
import sqlite3
import os

def main():

    global username 
    # create a secret key 
    key = Fernet.generate_key()
    with open(".key", "wb") as key_file:
        key_file.write(key)
    os.chmod(".key", 0o600) 

    # create a database 
    print("\nCreating a databse.")
    db = sqlite3.connect(".pass.db")
    pointer = db.cursor()
    pointer.execute("CREATE TABLE IF NOT EXISTS passwords (Id INTEGER PRIMARY KEY AUTOINCREMENT,label TEXT NOT NULL,username TEXT,password BLOB NOT NULL,date_created TEXT)")
    db.commit()
    db.close()
    print("Database created.\n")

    # Create a user login
    key = Fernet(key)
    username = input("Please provide a username: ") 
    with open(".user", "w") as name:
        name.write(username)    

    while True:
        # use get pass so the password is hidden
        password = getpass("Please provide a sepical password. This will be used to print all passwords: ")
        re_enter = getpass("Please re-enter the same password: ")

        # Check if the password is valid
        if password != re_enter:
            # if not prompt again
            print("Passwords does not match")
        else:
            # If ye then encrypt the password and save it
            with open(".pass", "wb") as passs:
                passs.write(key.encrypt(password.encode()))
            break

if __name__ == "__main__":
    main()

