import random
import string

def generate_password(grade_number):
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = '!@#$%^&*()_-+=<>?/[]{}|'

    # Combine all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Set the password length based on the chosen grade
    if grade_number < 1 or grade_number > 3:
        print("Invalid grade selection. Please choose a number from 1 to 3.")
        return None  

    if grade_number == 1: length = 10
    if grade_number == 2: length = 15
    if grade_number == 3: length = 20


    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
    print("Choose a password grade by entering the corresponding number:")
    print("1. Weak (10 characters)")
    print("2. Secure (15 characters)")
    print("3. Very Secure (20 characters)")
    
    try:
        grade_number = int(input("Enter the number of your desired password grade: "))
        password = generate_password(grade_number)
        
        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 3.")
