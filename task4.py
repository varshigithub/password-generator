import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4")

    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random choices from all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password += random.choices(all_characters, k=length-4)

    # Shuffle the resulting password list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and return it
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        password_length = int(input("Enter the length of each password: "))
        
        if num_passwords <= 0 or password_length <= 0:
            raise ValueError("Both the number of passwords and the length must be positive integers.")
        
        print("\nGenerated Passwords:")
        for _ in range(num_passwords):
            print(generate_password(password_length))

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
