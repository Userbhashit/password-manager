import os
from save import save 
from pyfiglet import Figlet
from setup import main as setup
from genrate import main as genrate 
from print_pass import main as print_all
from update import delete_pass, update_pass
from save_random import main as genrate_save    

def main():
    
    # If new user setup all the required files
    if not setedup():
        setup()

    welcome_user()

    # Keep asking user to choose
    while True:
        print()
        print("What would you like to do?")
        print("1.) Save a password,")
        print("2.) Genrate random passwords,")
        print("3.) Genrate random passwords and save one of them,")
        print("4.) Print all saved password and copy one,")
        print("5.) Update a password,")
        print("6.) Delete a password,")
        print("7.) Nuke the manager,")
        print("8.) Exit.")     

        choice = input("\nPlease enter the command number: ")

        match choice:
            case "1":
                save()
            case "2":
                genrate()
            case "3":
                genrate_save()
            case "4":
                print_all()
            case "5":
                update_pass()
            case "6":
                delete_pass()
            case "7":
                reset()
                print("See you soon...\n")
                return
            case "8":
                print("See you soon...\n")
                return
            case _:
                print("Please enter a number between 1 to 7")

# check if user have created logged in before or not
def setedup():
    return (os.path.exists(".key") and os.path.exists(".pass.db") and os.path.exists(".pass") and os.path.exists(".user"))

# Welcome user using figlet font
def welcome_user():
    print()
    f = Figlet(font="standard")
    with open(".user", "r") as name:
        username = name.read()
    welcome = f"Welcome  {username}"
    print(f.renderText(welcome))
    print()


# Check if a db already exist if it does delete it
def reset():
    try:
        os.remove(".key")
        os.remove(".pass")
        os.remove(".pass.db")
        os.remove(".user")
    except FileNotFoundError:
        pass

    print("\nPasswords deleted.\n")

if __name__ == "__main__":
    main()

