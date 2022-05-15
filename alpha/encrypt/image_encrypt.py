# import required module
from cryptography.fernet import Fernet

def key_gen():
    # key generation
    key = Fernet.generate_key()

    # string the key in a file
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)


def encrypt():
    # opening the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
      
    # using the generated key
    fernet = Fernet(key)
      
    # opening the original file to encrypt
    with open('pic.jpg', 'rb') as file:
        original = file.read()
          
    # encrypting the file
    encrypted = fernet.encrypt(original)
  
    # opening the file in write mode and 
    # writing the encrypted data
    with open('pic_encrypt.jpg', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decrypt():
    # opening the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    # using the key
    fernet = Fernet(key)

    # opening the encrypted file
    with open('pic_encrypt.jpg', 'rb') as enc_file:
        encrypted = enc_file.read()

    # decrypting the file
    decrypted = fernet.decrypt(encrypted)

    # opening the file in write mode and
    # writing the decrypted data
    with open('pic_decrypt.jpg', 'wb') as dec_file:
        dec_file.write(decrypted)


key_gen()
encrypt()
decrypt()
