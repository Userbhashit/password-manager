from genrate import generate, get_num_passwords
from cryptography.fernet import Fernet
import datetime
import sqlite3

def main():
    
    # get the list of passwords
    passwords = generate(get_num_passwords())
    
    # Print the list 
    print("Please choose a password from: ")
    for i in range(len(passwords)):
        print(f"{i+1}.) {passwords[i]}")
    print() 
    
    # Take user choice
    while True:
        try:
            choice = int(input("Which one to go with: "))

            if choice > len(passwords):
                raise IndexError
            elif choice == 0:
                return
            else:
                break

        except ValueError:
            print("Please enter a number or 0 to cancel.")
        except IndexError:
            print(f"Please enter a number between 1 to {len(passwords)}.")
    
    # Ask for other required details
    while True:
        try:
            label = input("Name of website or label: ").strip().lower()

            if not label:
                print("Please enter a website name or label")
                raise ValueError

            break
        except ValueError:
            continue

    user = input("UserName: ").strip()
    
    with open(".key", "rb") as key_file:
        key = key_file.read()
    key = Fernet(key)
    passwords = key.encrypt(passwords[choice-1].encode())
    date, time = str(datetime.datetime.now().replace(microsecond=0)).split(" ")
    created = f"{date} at {time}"
    
    # Connect to database
    db = sqlite3.connect(".pass.db")
    pointer = db.cursor()
    
    # Save the password
    pointer.execute("INSERT INTO passwords (label, username, password, date_created) VALUES (?, ?, ?, ?)", (label, user, passwords, created))
    db.commit()
    db.close()
    # Show confirmation
    print("\nPassword saved.\n")

if __name__ == "__main__":
    main()
