import sqlite3
import datetime
import getpass
from cryptography.fernet import Fernet

def save():
    website = input("Name of the website or label: ")

    while not website:
        print("Label cannot be empty.")
        website = input("Name of the website or label: ")

    username = input("username: ")

    password = getpass.getpass("password: ")
    while not password:
        print("Password cannot be empty.")
        password = input("password: ")

    with open(".key", "rb") as key_file:
        key = key_file.read()

    key = Fernet(key)
    password = key.encrypt(password.encode())
        
    date, time = str(datetime.datetime.now().replace(microsecond=0)).split(" ") 
    created = f"{date} at {time}"

    db = sqlite3.connect(".pass.db")
    pointer = db.cursor()
    pointer.execute("INSERT INTO passwords(label, username, password, date_created) VALUES (?, ?, ?, ?)", (website, username, password, created))
    db.commit()
    db.close()

if __name__ == "__main__":
    save()

