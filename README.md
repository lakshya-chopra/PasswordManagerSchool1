# Password Manager 

- This is a basic Password manager with built-in password generator that allows a user to safely secure their passwords with the help of cryptographic methods. All the data is stored in MySQL database.

- I have used the rich module as well to make an intuitive and interesting terminal based UI.

- Additionally, I’ve made use of **SHA256** hashing algorithm for safely hashing the master password and PBKDF2 (making use of SHA512) to derive a cryptographic key that will be used in encryption and decryption of the passwords.
Encryption carried out using **AES256**.

(Will add more relevant info later)

## Modules used:
   ### 3rd party 
    - Rich
    - mysql-connector-python
    - PyCryptoDome
    
   ### Built-in 
    - getpass
    - base64
    - strings
    - secrets

## Output SCREENS:
![image](https://github.com/lakshya-chopra/PasswordManagerSchool1/assets/77010972/0e347169-3b46-448a-a920-689ca2947af3)
![image](https://github.com/lakshya-chopra/PasswordManagerSchool1/assets/77010972/db8825b2-b2e2-4721-9e27-a738aed62f83)

![image](https://github.com/lakshya-chopra/PasswordManagerSchool1/assets/77010972/f352ec6a-dad1-4465-985c-49f1ac9a9b8b)

![image](https://github.com/lakshya-chopra/PasswordManagerSchool1/assets/77010972/dd52508f-e567-49b5-8899-cadc68cd3180)


## Installation:  
   - Make sure you have MySQL server installed and a registered account. [Check the installation website](https://dev.mysql.com/doc/refman/5.7/en/installing.html)
   - Python version >= 3.7.0
   - Install all the required modules using `pip install -r requirements.txt`
   - Replace the dummy passwd string in database connector with your own MySQL local account password. (See database_manager.py file)
   - Navigate to `src`, run main.py and start experimenting :) 💯.

*Credits to https://github.com/teja156/ for the aesutil.py file.*

