import sqlite3
from getpass import getpass
from cryptography.fernet import Fernet

def main():
    update_pass()
    delete_pass()

def update_pass():
    label_or_id = input("Would you like to update using??\nPress '1' for id or '2' for label/website name or anyother key to cancel: ")

    if label_or_id == "1":
        update_id()
        return
    elif label_or_id == "2":
        update_label()
    else:
        return

def update_id():
    db = sqlite3.connect(".pass.db")
    pointer = db.cursor()

    max_id = pointer.execute("SELECT COUNT(*) FROM passwords").fetchone()[0]

    if max_id == 0:
        print("Table is empty.")
        return

    id_to_update = int(input("Id: "))

    # Check if ID exists
    result = pointer.execute("SELECT label FROM passwords WHERE id = ?", (id_to_update,)).fetchone()
    if result is None:
        print(f"Id: {id_to_update} does not exist.")
        return

    label = result[0]
    confirm = input(f"Update password for {label}? (y/n): ")

    if confirm.lower() in ["y", "yes"]:
        password = getpass("Enter the new password: ")

        with open(".key", "rb") as key_file:
            key = key_file.read()

        key = Fernet(key)
        pass_encpt = key.encrypt(password.encode())
        pointer.execute("UPDATE passwords SET password = ? WHERE id = ?", (pass_encpt, id_to_update))

        db.commit()
        db.close()

        print(f"Password for {label} updated.")
    else:
        print("Cancelled.")
        db.close()

def update_label():
    db = sqlite3.connect(".pass.db")
    pointer = db.cursor()

    label = input("Enter the website/label name: ").strip()

    result = pointer.execute("SELECT id FROM passwords WHERE label = ?", (label,)).fetchone()
    if result is None:
        print(f"No entry found for label: {label}")
        db.close()
        return

    id_to_update = result[0]

    confirm = input(f"Update password for '{label}'? (y/n): ")
    if confirm.lower() not in ["y", "yes"]:
        print("Cancelled.")
        db.close()
        return

    password = getpass("Enter the new password: ")

    with open(".key", "rb") as key_file:
        key = key_file.read()

    key = Fernet(key)
    pass_encpt = key.encrypt(password.encode())
    pointer.execute("UPDATE passwords SET password = ? WHERE id = ?", (pass_encpt, id_to_update))

    db.commit()
    db.close()

    print(f"Password for {label} updated.")

def delete_pass():
    method = input("Delete by:\nPress '1' for ID or '2' for label/website name (or any other key to cancel): ")

    if method == "1":
        delete_by_id()
    elif method == "2":
        delete_by_label()
    else:
        print("Cancelled.")

def delete_by_id():
    db = sqlite3.connect(".pass.db")
    pointer = db.cursor()

    max_id = pointer.execute("SELECT COUNT(*) FROM passwords").fetchone()[0]
    if max_id == 0:
        print("Table is empty.")
        db.close()
        return

    try:
        id_to_delete = int(input("Enter the ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        db.close()
        return

    row = pointer.execute("SELECT label FROM passwords WHERE id = ?", (id_to_delete,)).fetchone()
    if row is None:
        print(f"No entry found for ID {id_to_delete}")
        db.close()
        return

    label = row[0]
    confirm = input(f"Are you sure you want to delete password for '{label}' (ID {id_to_delete})? (y/n): ")

    if confirm.lower() in ["y", "yes"]:
        pointer.execute("DELETE FROM passwords WHERE id = ?", (id_to_delete,))
        db.commit()
        print("Entry deleted.")
    else:
        print("Cancelled.")

    db.close()

def delete_by_label():
    db = sqlite3.connect(".pass.db")
    pointer = db.cursor()

    label = input("Enter the label/website name to delete: ").strip()

    result = pointer.execute("SELECT id FROM passwords WHERE label = ?", (label,)).fetchone()
    if result is None:
        print(f"No entry found for label '{label}'")
        db.close()
        return

    id_to_delete = result[0]
    confirm = input(f"Are you sure you want to delete password for '{label}' (ID {id_to_delete})? (y/n): ")

    if confirm.lower() in ["y", "yes"]:
        pointer.execute("DELETE FROM passwords WHERE id = ?", (id_to_delete,))
        db.commit()
        print("Entry deleted.")
    else:
        print("Cancelled.")

    db.close()

if __name__ == "__main__":
    main()
