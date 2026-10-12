"""
Secure Password Generator
-------------------------
A simple command-line tool that generates random passwords based on
the length and character types you choose.

Uses Python's built-in `secrets` module, which is designed for
cryptographically secure random values.
"""

import secrets
import string


def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    """Generates a random password based on user preferences."""
    # Build the list of allowed character groups based on user settings
    groups = []
    if use_lowercase:
        groups.append(string.ascii_lowercase)
    if use_uppercase:
        groups.append(string.ascii_uppercase)
    if use_numbers:
        groups.append(string.digits)
    if use_symbols:
        groups.append(string.punctuation)

    # Prevent a crash if the user turns off all character options
    if not groups:
        print("Error: You must select at least one character type.")
        return None

    character_pool = "".join(groups)

    # Guarantee at least one character from every selected group
    password_chars = [secrets.choice(group) for group in groups]

    # Fill the remaining length with random characters from the full pool
    password_chars += [
        secrets.choice(character_pool) for _ in range(length - len(password_chars))
    ]

    # Shuffle so the guaranteed characters are not always at the start
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def get_boolean_input(prompt):
    """Helper function to safely get a Yes/No answer from the user."""
    # Loop until the user gives a valid answer
    while True:
        choice = input(prompt).strip().lower()
        if choice in ["y", "yes"]:
            return True
        elif choice in ["n", "no"]:
            return False
        else:
            print("Invalid input. Please enter 'y' for Yes or 'n' for No.")


def main():
    """Main application flow."""
    print("--- SECURE PASSWORD GENERATOR ---")

    # 1. Get and validate the desired password length
    while True:
        try:
            length = int(input("Enter total password length (minimum 4): "))
            if length >= 4:
                break
            print("Password must be at least 4 characters long for basic security.")
        except ValueError:
            print("Please enter a valid whole number.")

    # 2. Get user preferences for password strength
    print("\nCustomize your password settings:")
    include_upper = get_boolean_input("Include uppercase letters? (y/n): ")
    include_lower = get_boolean_input("Include lowercase letters? (y/n): ")
    include_nums = get_boolean_input("Include numbers? (y/n): ")
    include_syms = get_boolean_input("Include symbols/special characters? (y/n): ")

    # 3. Generate and display the final password
    password = generate_password(
        length, include_upper, include_lower, include_nums, include_syms
    )

    if password:
        print("\n" + "=" * 30)
        print(f" Your Secure Password: {password}")
        print("=" * 30)


# Run main() only when the script is executed directly, not when imported
if __name__ == "__main__":
    main()
