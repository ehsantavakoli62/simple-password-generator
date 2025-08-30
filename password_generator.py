# A simple password generator script
import random
import string

def generate_password(length=12):
    """Generates a random password with letters, numbers, and symbols."""
    
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Check if the length is a positive number
    if length <= 0:
        return "Password length must be a positive number."
    
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage
if __name__ == "__main__":
    generated_password = generate_password()
    print("Generated Password:", generated_password)
