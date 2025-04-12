import secrets

# Character sets
LETTERS_LOWER = "abcdefghijklmnopqrstuvwxyz"
LETTERS_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SYMBOLS = "!#$%&()*+"

def main():
    # Get number of passwords to genrate from user
    num_password = get_num_passwords()
    passwords = generate(num_password) # Genrate n random passwords 
    
    # print them to user
    for i, pwd in enumerate(passwords, 1):
        print(f"{i}). {pwd}")

def generate(num_password) -> list[str]:
    passwords = []
    length = get_length()

    print("\nHere are your passwords:\n")

    for _ in range(num_password):
        password_chars = []

        num_symbols = secrets.choice([1, 2])
        num_upper = secrets.choice([1, 2])
        num_numbers = secrets.choice([1, 2])
        num_lower = length - (num_symbols + num_upper + num_numbers)
        num_lower = max(0, num_lower)  # avoid negative

        password_chars += [secrets.choice(SYMBOLS) for _ in range(num_symbols)]
        password_chars += [secrets.choice(LETTERS_UPPER) for _ in range(num_upper)]
        password_chars += [secrets.choice(LETTERS_LOWER) for _ in range(num_lower)]
        password_chars += [secrets.choice(NUMBERS) for _ in range(num_numbers)]

        # Shuffle using secrets-based method
        secrets.SystemRandom().shuffle(password_chars)
        passwords.append(''.join(password_chars))

    return passwords

def get_num_passwords():
    while True:
        try:
            return int(input("How many passwords do you want to generate? "))
        except ValueError:
            print("Please enter a valid number.")

def get_length():
    while True:
        try:
            length = int(input("Length of each password (more than 7): "))
            if length <= 7:
                raise IndexError
            return length
        except ValueError:
            print("Please enter a valid number.")
        except IndexError:
            print("Password length must be more than 7.")

if __name__ == "__main__":
    main()
