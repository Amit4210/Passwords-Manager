from cryptography.fernet import Fernet  # required to encrypt text

# def write_key():
#     key = Fernet.generate_key()
#     with open('key.key', 'wb') as key_file:
#         key_file.write(key)


def load_key():
    file = open('key.key', 'rb')
    rkey = file.read()
    file.close()
    return rkey


# mstr_pwd = input('Enter the master password: ')

key = load_key() # mstr_pwd.encode()
fer = Fernet(key) # initializing the encryption module


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split(" | ")
            print(f'Username: {user}, Password: {fer.decrypt(passw.encode()).decode()}')


def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(name + ' | ' + fer.encrypt(pwd.encode()).decode() + '\n')



while True:
    mode = input('Do you want to add a password or view the existing ones? (view, add, q to quit):')
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid Mode.')
