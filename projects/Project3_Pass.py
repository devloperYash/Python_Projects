import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_special=True):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special = string.punctuation if use_special else ''

    # Combine character sets
    all_characters = lowercase + uppercase + numbers + special

    if not all_characters:
        return "Error: No character sets selected."

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def password_generator_app():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Error: Password length must be a positive integer.")
            return
        
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, use_uppercase, use_numbers, use_special)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Error: Please enter a valid number for the password length.")

# Run the password generator
password_generator_app()
