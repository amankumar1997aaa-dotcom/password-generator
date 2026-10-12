# Secure Password Generator

A simple command-line tool written in Python that generates strong random passwords. You choose the length and which character types to include.

## Features

- Custom password length (minimum 4 characters)
- Choose uppercase letters, lowercase letters, numbers, and symbols
- Guarantees at least one character from every type you select
- Uses Python's `secrets` module for cryptographically secure randomness
- Input validation, so bad input never crashes the program
- No external libraries needed

## Requirements

- Python 3.6 or higher

## Installation

```bash
git clone https://github.com/YOUR-USERNAME/password-generator.git
cd password-generator
```

## Usage

```bash
python password_generator.py
```

## Example

```
--- SECURE PASSWORD GENERATOR ---
Enter total password length (minimum 4): 12

Customize your password settings:
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols/special characters? (y/n): y

==============================
 Your Secure Password: k#9Tq!aW2zL@
==============================
```

## How it works

1. Asks for the password length and validates it.
2. Asks which character types to include (yes/no).
3. Builds a pool of allowed characters from the selected types.
4. Picks one character from each selected type, fills the rest randomly from the full pool, then shuffles everything.
5. Prints the final password.

## Project structure

```
password-generator/
├── password_generator.py
├── README.md
├── LICENSE
└── .gitignore
```

## Tips for a strong password

- Use 12 or more characters.
- Turn on all four character types.
- Never reuse the same password on different websites.
- Store passwords in a password manager.

## Future improvements

- Copy the password to the clipboard automatically
- Generate multiple passwords at once
- Add a password strength meter
- Build a GUI version

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
