import base64
import os
from random import randrange
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from cryptography.fernet import Fernet, InvalidToken

input_file = input("Place the file here to decrypt/encrypt can be any file lower than your system memory:\n> ")
output_file = input("the name of the output file:\n> ") + ".txt"

pasword_provide = "password"
password = pasword_provide.encode() 

salt = b'?\x17\x8b\x05\x0c\x00h\x1c2\xd5\xf3:m\x0e\x1f\x10'
kdf = PBKDF2HMAC(hashes.SHA3_256(),32,salt,100000,default_backend())
key = base64.urlsafe_b64encode(kdf.derive(password))

def encrypt_file():
    with open(input_file, 'rb') as f:
        data = f.read() 

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)  # Write the encrypted bytes to the output file
        print("> encrypted data: ",encrypted)
        sys()
        
def decrypt_file():
    with open(output_file, 'rb') as f:
        data = f.read()  # Read the bytes of the encrypted file

    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(data)
        print(decrypted)
        with open(input_file, 'wb') as f:
            f.write(decrypted)  # Write the decrypted bytes to the output file
            print(decrypted)
            sys()
        # Note: You can delete input_file here if you want
    except InvalidToken as e:
        print("Invalid Key - Unsuccessfully decrypted")
        sys()

def sys():
    value = input("> ")
    if value == "en":
        encrypt_file()

    elif value == "de":
        decrypt_file()
    elif value == "kill":
        print("> program killed ;-;")
        exit()
    else:
        sys()

print("> Type 'de' to decrypt")
print("> Type 'en' to encrypt")
sys()


