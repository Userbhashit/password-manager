from save import save 
from pyfiglet import Figlet
from genrate import main as genrate 
from print_pass import main as print_all
from save_random import main as genrate_save    

def main():

    print()
    f = Figlet(font="standard")
    with open(".user", "r") as name:
        username = name.read()
    welcome = f"Welcome  {username}"
    print(f.renderText(welcome))
    print()
    
    print("What would you like to do?")
    print("1.) Save a password,")
    print("2.) Genrate random passwords,")
    print("3.) Genrate random passwords and save one of them,")
    print("4.) Print all saved password and copy one,")
    print("5.) Update or delete or search a password,")
    print("6.) exit.")

    while True:
        choice = input("\nPlease enter the command number: ")

        match choice:
            case "1":
                print("Implementing...")
            case "2":
                genrate()
            case "3":
                genrate_save()
            case "4":
                print_all()
            case "5":
                save()
            case "6":
                print("See you soon...\n")
                return
            case _:
                print("Please enter a number between 1 to 6")


if __name__ == "__main__":
    main()
