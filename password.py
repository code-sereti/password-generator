import random
import string

def generate_strong_password(length=12):
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure at least one character from each set
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Generate the rest of the password
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the password characters
    random.shuffle(password)

    # Convert the list to a string
    password_str = ''.join(password)

    return password_str

# Example usage: generate a strong password of length 16
strong_password = generate_strong_password(16)
print("Generated Strong Password:", strong_password)
