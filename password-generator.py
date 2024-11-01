import random

def create_passwords(num_passwords, length, include_numbers, include_special_chars, language_chars):
    passwords = []
    available_chars = language_chars

    if include_numbers:
        available_chars += '0123456789'
    if include_special_chars:
        available_chars += '!@#$%^&*()-_'

    for password_index in range(num_passwords):
        password = ''
        
        for char_index in range(length):
            password += random.choice(available_chars)
        
        passwords.append(password)
    
    return passwords

def get_number_input(user_prompt, min_value, max_value):
    while True:
        try:
            user_input = int(input(user_prompt))
            if user_input < min_value or user_input > max_value:
                print(f"Please enter a number between {min_value} and {max_value}.")
            else:
                return user_input
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_yes_or_no(user_prompt):
    while True:
        answer = input(user_prompt).lower()
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            print("Please answer with 'yes' or 'no'.")

def choose_language_characters():
    language_chars = ''
    
    if get_yes_or_no("Include Punjabi characters (yes/no)? "):
        language_chars += "ਅਆਇਈਉਊਏਐਓਔਕਖਗਘਙਚਛਜਝਞਟਠਡਢਣਤਥਦਧਨਪਫਬਭਮਯਰਲਵਸ਼ਸਹਲ਼ੳੲੴ"
    if get_yes_or_no("Include Hindi characters (yes/no)? "):
        language_chars += "अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह"
    if get_yes_or_no("Include Tamil characters (yes/no)? "):
        language_chars += "அஆஇஈஉஊஎஏஐஒஓஔகஙசஞடணதநபமயரலவழளறன"

    if language_chars == '':
        print("At least one language must be selected! Defaulting to English letters.")
        language_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    return language_chars

def main():
    print("Welcome to Indic Password Generator!")

    num_passwords = get_number_input("How many passwords would you like to generate (1-10)? ", 1, 10)
    length = get_number_input("Enter the number of characters for each password (12-64): ", 12, 64)
    include_numbers = get_yes_or_no("Include numbers (yes/no)? ")
    include_special_chars = get_yes_or_no("Include special characters (yes/no)? ")
    language_chars = choose_language_characters()

    passwords = create_passwords(num_passwords, length, include_numbers, include_special_chars, language_chars)

    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, 1):
        print("Password", i, ":", password)

main()