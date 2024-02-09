# Password Manager 

This is a basic Password manager with built-in password generator that allows a user to safely secure their passwords with the help of cryptographic methods.. All the data is stored in MySQL database.

I have used the rich module as well to make an intuitive and interesting terminal based UI.

Additionally, I’ve made use of SHA512 hashing algorithm for safely hashing the master password and PBKDF2 to derive a cryptographic key that will be used in encryption and decryption of the passwords.

## Modules used:
    - Rich
    - Secrets (available in python std library)
    - PyCrypto
    - mysql-connector-python
    
    
