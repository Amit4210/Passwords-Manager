# Password Manager

A simple command-line password manager that encrypts and stores your passwords securely using the Fernet encryption scheme from the `cryptography` library.

## Features

- **Secure Encryption**: Uses Fernet symmetric encryption to protect your passwords
- **Simple Interface**: Command-line interface for adding and viewing passwords
- **Local Storage**: Passwords are stored locally in an encrypted format

## Requirements

- Python 3.x
- `cryptography` library

## Installation

1. Install the required dependency:
```bash
pip install cryptography
```

2. Generate an encryption key (run this once before first use):
```python
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

write_key()
```

## Usage

Run the script and choose from the following options:

- **add**: Add a new password entry
- **view**: Display all stored passwords (decrypted)
- **q**: Quit the application

### Adding a Password
1. Select `add` when prompted
2. Enter the account name
3. Enter the password to store
4. The password will be encrypted and saved

### Viewing Passwords
1. Select `view` when prompted
2. All stored passwords will be displayed in decrypted format

## File Structure

- `passwords.txt`: Contains encrypted password entries in the format `account_name | encrypted_password`
- `key.key`: Contains the encryption key (keep this file secure!)

## Security Notes

⚠️ **Important Security Considerations:**

- **Key Management**: The `key.key` file contains your encryption key. If you lose this file, you cannot decrypt your passwords. Keep it secure and backed up.
- **Local Storage**: Passwords are stored locally. This script does not include network transmission, but ensure your local environment is secure.
- **No Master Password**: The current implementation doesn't use a master password. Consider adding this feature for additional security.
- **Backup**: Regularly backup both `key.key` and `passwords.txt` files.

## Limitations

- No master password protection
- Basic error handling
- Passwords are displayed in plain text when viewing
- No password strength validation
- No search functionality

## Improvements for Production Use

Consider adding:
- Master password authentication
- Password strength validation
- Search and edit functionality
- Better error handling
- Secure clipboard integration
- Password generation features
- Database storage instead of text files
