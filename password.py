# **********************************   ***** Generate Random Password *****   ************************

import random , string


def generate_password(length=8):
    """Generate a random password with the specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    return password


if __name__ == "__main__":
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print(f"Your password is: {password}")